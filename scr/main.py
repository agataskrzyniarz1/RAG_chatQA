from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI
from pybtex.database import parse_file
from pybtex.style.formatting import plain
from pybtex.plugin import find_plugin
import getpass
import os
import shutil
from typing import List
import argparse
import re

# Paths
main_path = "../data/final/main.md"
bib_path = "../data/final/biblio.bib"
chroma_path = "../chroma"

CITATION_REGEX = re.compile(r"\[@([A-Za-z0-9:\-_]+)\]")

# === Load and concatenate files ===

def load_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_corpus(main_path: str) -> str:
    """Load main.md as corpus."""
    return load_file(main_path)

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


# === Extract citation keys ===

def extract_citation_keys(text: str) -> List[str]:
    return list({m.group(1) for m in CITATION_REGEX.finditer(text)})


# === Format bibliography entries ===

class PybtexFormatter:
    """
    Formats citations from a .bib file in plain style (authors. title. publisher, year.)
    """
    def __init__(self, bib_path: str):
        self.bib_data = parse_file(bib_path)
        self.formatter = plain.Style()
        self.backend = find_plugin('pybtex.backends', 'text')()

    def format_entry(self, key: str) -> str:
        if key not in self.bib_data.entries:
            return f"[Reference not found for key: {key}]"
        entry = self.bib_data.entries[key]
        formatted = self.formatter.format_entries([entry])
        for fe in formatted:
            return fe.text.render(self.backend)

    def format_all(self):
        citations = []
        for key in self.bib_data.entries:
            citations.append(self.format_entry(key))
        return citations
    

def extract_used_sources(answer_text: str, formatter: PybtexFormatter) -> List[str]:
    """
    It analyzes the LLM response and returns a list of citations whose authors appear in the text.
    The match is case-insensitive and only as a separate word.
    """
    used_keys = set()
    bib_data = formatter.bib_data

    for key, entry in bib_data.entries.items():
        for person in entry.persons.get("author", []):
            last_name = person.last_names[0]
            pattern = r'\b' + re.escape(last_name) + r'\b'
            if re.search(pattern, answer_text, flags=re.IGNORECASE):
                used_keys.add(key)

    return [formatter.format_entry(key) for key in used_keys]


# === Insert OpenAI API key if needed ===

def set_openai_api_key():
    """Prompt for OpenAI API key if not already in environment variables."""
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")


# === Main ===

def main():
    set_openai_api_key()

    # Load corpus
    corpus_text = load_corpus(main_path)
    #print("Corpus loaded.")

    # Load bibliography
    formatter = PybtexFormatter(bib_path)

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
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.5:
        print(f"Unable to find matching results.")
        return
    
    context_text = "\n---\n".join([doc.page_content for doc, _score in results])
    
    #print("\nContext:\n")
    #print(context_text)
    #print("\n---\n")
    
    # Citation keys from retrieved context
    found_keys = extract_citation_keys(context_text)

    # Prompt
    PROMPT = (
    "You are answering a question based strictly on the provided CONTEXT, which comes from an academic thesis. "
    "Use inline citations in the form (Author, Year) ONLY when the context contains citation keys like [@tarone-2006]."
    "Do NOT make up new sources. Do not hallucinate bibliography entries."
    "If the question is not related to the CONTEXT, do NOT attempt to answer it; instead, clearly say "
    "'This question is not related to the provided thesis context.'\n\n"
    f"CONTEXT:\n{context_text}\n\n"
    f"QUESTION:\n{query_text}\n\n"
    "Provide a clear, concise answer:"
)

    # Call the LLM
    client = OpenAI()

    response = client.responses.create(
        model="gpt-4o-mini",
        input=query_text,
        instructions=PROMPT
    )

    answer = response.output_text.strip()

    # Print the answer
    print("Response:\n")
    print(answer)

    # Print references if any
    sources = extract_used_sources(answer, formatter)
    if sources:
        print("\nSources:\n")
        for s in sources:
            print(f"{s}")
            print()


    #for i, doc in enumerate(structured_docs):
    #    print(f"Doc {i}: {doc.metadata}")


if __name__ == "__main__":
    main()

