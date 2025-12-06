from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI
import getpass
import os
import shutil
from typing import List
import argparse

# Paths
main_path = "../data/final/main.md"
bib_path = "../data/final/biblio.bib"
chroma_path = "../chroma"


# === Load and concatenate files ===

def load_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_corpus(main_path: str, bib_path: str) -> str:
    """Load main.md and biblio.bib and concatenate them."""
    main_text = load_file(main_path)
    bib_text = load_file(bib_path)
    return main_text + "\n\n" + bib_text

# === Split by Markdown structure ===

def build_header_path(metadata):
    """Build header path from metadata: create 'Header1 > Header2 > Header3' string."""
    levels = ["Header 1", "Header 2", "Header 3", "Header 4"]
    headers = [metadata[level] for level in levels if metadata.get(level)]
    return "Headers: " + " > ".join(headers)

def split_markdown(corpus_text: str) -> List[Document]:
    """
    Split corpus text by Markdown headers, preserving tables, lists, code blocks.
    Returns a list of Documents.
    """
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
            ("####", "Header 4"),
        ]
    )

    sections = markdown_splitter.split_text(corpus_text)

    structured_docs = []

    for sec in sections:
        header_path = build_header_path(sec.metadata)

        structured_docs.append(
            Document(
                page_content=sec.page_content,
                metadata={"header_path": header_path}
            )
        )

    return structured_docs

# === Recursive chunking with metadata (headers) ===

def chunk_documents(structured_docs: List[Document], chunk_size: int = 1800, chunk_overlap: int = 200) -> List[Document]:
    """
    Split structured Documents into smaller chunks recursively.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True,
    )

    all_chunks = []

    for doc in structured_docs:
        chunks = text_splitter.create_documents([doc.page_content])

        header_path = doc.metadata["header_path"]

        # Repeat header path twice to boost embedding importance
        header_boost = f"{header_path}\n{header_path}\n\n"

        for chunk in chunks:
            # Add header path to metadata
            chunk.metadata["header_path"] = header_path

            # Prepend boosted header path
            chunk.page_content = f"{header_boost}{chunk.page_content}"

            all_chunks.append(chunk)

    return all_chunks


# === Create Chroma vectorstore ===

def create_vectorstore(chunks: List[Document], persist_dir: str = chroma_path) -> Chroma:
    """
    Create a Chroma vectorstore from chunked documents using OpenAI embeddings.
    If the persist_dir exists, it is cleared first.
    """
    if os.path.exists(persist_dir):
        shutil.rmtree(persist_dir)

    db = Chroma.from_documents(
        chunks,
        OpenAIEmbeddings(),
        persist_directory=persist_dir
    )
    #print(f"Saved {len(chunks)} chunks to {persist_dir}.")
    return db

# === Insert OpenAI API key if needed ===

def set_openai_api_key():
    """Prompt for OpenAI API key if not already in environment variables."""
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")


# === Main ===

def main():
    set_openai_api_key()

    # Load corpus
    corpus_text = load_corpus(main_path, bib_path)
    #print("Corpus loaded.")

    # Split by Markdown
    structured_docs = split_markdown(corpus_text)
    #print(f"Structured blocks: {len(structured_docs)}")

    # Chunking
    chunks = chunk_documents(structured_docs)
    #print(f"Final chunks: {len(chunks)}")

    # Create vectorstore
    db = create_vectorstore(chunks)

    # Inspect chunks
    #for i, doc in enumerate(chunks[:20], start=1):
    #    print(f"\n--- Chunk {i} ---")
    #    print(doc.page_content)

    # Create CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The question.")
    args = parser.parse_args()
    query_text = args.query_text

    # Prepare the DB
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=chroma_path, embedding_function=embedding_function)

    # Search the DB
    results = db.similarity_search_with_relevance_scores(query_text, k=4)
    if len(results) == 0 or results[0][1] < 0.5:
        print(f"Unable to find matching results.")
        return
    
    context_text = "\n---\n".join([doc.page_content for doc, _score in results])
    
    #print("\nContext:\n")
    #print(context_text)
    #print("\n---\n")

    # Prompt template
    PROMPT_TEMPLATE = f"Answer the question based only on the following context: {context_text}."

    # Call the LLM
    client = OpenAI()

    response = client.responses.create(
        model="gpt-4o-mini",
        input=query_text,
        instructions=PROMPT_TEMPLATE
    )

    print("Response:\n")
    print(response.output_text)


    #for i, doc in enumerate(structured_docs):
    #    print(f"Doc {i}: {doc.metadata}")


if __name__ == "__main__":
    main()
