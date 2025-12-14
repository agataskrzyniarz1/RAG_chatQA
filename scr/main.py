from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_core.documents import Document
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

# Regex
CITATION_BLOCK_REGEX = re.compile(r"\[@([^\]]+)\]")
CITATION_KEY_REGEX = re.compile(r"@([^\s;,\]]+)")

# === Load corpus ===

def load_corpus(main_path: str) -> str:
    """Load main.md as corpus."""
    with open(main_path, "r", encoding="utf-8") as f:
        return f.read()

# == Extract front matter (front page) - not embedding-friendly ==    

def extract_front_matter(corpus_text: str) -> str:
    match = re.search(r"---\s*(.*?)\s*## Abstract", corpus_text, re.DOTALL)
    return match.group(1) if match else ""


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

def chunk_documents(structured_docs: List[Document], chunk_size: int = 2000, chunk_overlap: int = 200) -> List[Document]:
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
    keys = []
    for block in CITATION_BLOCK_REGEX.findall(text):
        found = CITATION_KEY_REGEX.findall(block)
        keys.extend(found)
    return list(set(keys))


# === Bibliography ===

class PybtexFormatter:
    """
    Format citations from a .bib file in plain style (authors. title. publisher, year.)
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
    

def get_author_year(formatter: PybtexFormatter, key: str):
    if key not in formatter.bib_data.entries:
        return None, None

    entry = formatter.bib_data.entries[key]
    authors = entry.persons.get("author", [])
    if len(authors) == 0:
        author = "Unknown"
    else:
        author = authors[0].last_names[0]

    year = entry.fields.get("year", "n.d.")
    return author, year

def replace_citations_with_author_year(answer_text: str, formatter: PybtexFormatter):

    def repl(match):
        inside = match.group(1)

        # Split by semicolon, comma, or whitespace
        raw_parts = re.split(r'[;,\s]+', inside)

        keys = []
        for part in raw_parts:
            if not part:
                continue
            key = part.lstrip('@').strip()
            if key:
                keys.append(key)

        citations = []

        for key in keys:
            entry = formatter.bib_data.entries.get(key)
            if entry is None:
                citations.append("")
                continue

            # Extract authors
            persons = entry.persons.get("author", [])
            lastnames = [p.last_names[0] for p in persons] if persons else []

            # Format author string
            if len(lastnames) == 0:
                author_str = "Unknown"
            elif len(lastnames) == 1:
                author_str = lastnames[0]
            elif len(lastnames) == 2:
                author_str = f"{lastnames[0]} and {lastnames[1]}"
            else:
                author_str = f"{lastnames[0]} et al."

            # Extract year
            year = entry.fields.get("year", "n.d.")

            citations.append(f"({author_str}, {year})")

        if not citations:
            return match.group(0)

        # If multiple citations → "(A, Y) (B, Y)"
        return " ".join(citations)

    # Replace all [@...] blocks
    return CITATION_BLOCK_REGEX.sub(repl, answer_text)


# === References ===

def extract_used_sources(answer_text: str, formatter: PybtexFormatter) -> List[str]:
    """
    Extract used references by matching (Author, Year),
    using only the first author's last name from both the citation and BibTeX.
    """

    # Match citations
    citation_pattern = re.compile(r"\(([^,]+),\s*([0-9]{4}|n\.d\.)\)")
    matches = citation_pattern.findall(answer_text)

    used_keys = set()

    for author_block, year in matches:

        # Normalize year
        year = year.strip()

        # Extract first surname from the author block
        first_author = author_block.split("and")[0].split("et al.")[0].strip()
        first_author = first_author.lower()

        # Search BibTeX for matching entry
        for key, entry in formatter.bib_data.entries.items():
            persons = entry.persons.get("author", [])
            if not persons:
                continue

            # First author's last name from .bib
            bib_lastname = persons[0].last_names[0].lower()
            bib_year = entry.fields.get("year", "n.d.")

            if bib_lastname == first_author and bib_year == year:
                used_keys.add(key)

    return [formatter.format_entry(key) for key in used_keys]


# === Insert OpenAI API key if needed ===

def set_openai_api_key():
    """Prompt for OpenAI API key if not already in environment variables."""
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")


# === Global initialization ===

set_openai_api_key()

# Load corpus
corpus_text = load_corpus(main_path)
#print("Corpus loaded.")

# Load front matter
front_matter = extract_front_matter(corpus_text)
#print(front_matter)

front_doc = Document(
    page_content=(
        "This is the title page and metadata of the thesis.\n"
        + front_matter
    ),
    metadata={"header_path": "Front Matter > Title Page"}
)

# Load bibliography
formatter = PybtexFormatter(bib_path)
#print(formatter.bib_data.entries.keys())

# Split by Markdown
structured_docs = split_markdown(corpus_text)
structured_docs.insert(0, front_doc)
#print(f"Structured blocks: {len(structured_docs)}")

# Chunking
chunks = chunk_documents(structured_docs)
#print(f"Final chunks: {len(chunks)}")

# Create vectorstore
db = create_vectorstore(chunks)

# Inspect chunks
#for i, doc in enumerate(chunks[:5], start=1):
#    print(f"\n--- Chunk {i} ---")
#    print(doc.page_content)

# Prepare the DB
embedding_function = OpenAIEmbeddings()
db = Chroma(persist_directory=chroma_path, embedding_function=embedding_function)

# == RAG function ==

def get_rag_answer(question: str):
    
    # Search the DB
    results = db.similarity_search_with_relevance_scores(question, k=4)

    if not results or results[0][1] < 0.5:
        return "Unable to find relevant context in the thesis", []
    
    docs = [doc for doc, _score in results]
    
    context_text = "\n---\n".join(doc.page_content for doc in docs)

    context_for_eval = list(doc.page_content for doc in docs)

    # Citation keys from retrieved context
    #found_keys = extract_citation_keys(context_text)

    # Prompt
    PROMPT = f"""
    You are answering a question based strictly on the provided CONTEXT, which comes from a master's thesis.
    The CONTEXT may contain chapter or section headers; these headers are metadata only and must NOT be mentioned, paraphrased, or used as sources in your answer.

    When citing, always use the original citation tags from the context (don't change their form).
    Do NOT cite chapter titles, section names, or headers.
    Use all citation tags that are relevant to your answer.
    Do NOT invent new citation keys.
    If the question is not related to the CONTEXT, do NOT attempt to answer it; instead, clearly say:
    'This question is not related to the provided thesis context.'

    CONTEXT:
    
    {context_text}

    QUESTION:

    {question}

    Provide a clear answer:
    """

    # Call the LLM
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o-mini",
        input=PROMPT
    )
    raw_answer = response.output_text.strip()

    #print("\nRaw answer:\n")
    #print(raw_answer)
    #print("\n")

    answer = replace_citations_with_author_year(raw_answer, formatter)
    return answer, context_text, context_for_eval


# === CLI ===

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("question", type=str, help="Question for the RAG system")
    args = parser.parse_args()

    answer, context, context_for_eval = get_rag_answer(args.question)

    # Print the context
    #print("\nContext:\n")
    #print(context)
    #print("\n---\n")

    # Print the answer
    print("Response:\n")
    print(answer)

    # Print references if any
    sources = extract_used_sources(answer, formatter)
    if sources:
        print("\nReferences:\n")
        for s in sources:
            print(f"{s}")
            print()
