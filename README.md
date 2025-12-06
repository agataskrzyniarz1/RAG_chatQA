# RAG-Thesis-Chatbot

This repository contains a Retrieval-Augmented Generation (RAG) project — an interactive question-answering chatbot answering questions about my master thesis:

> Performance Evaluation of Tools for Automatic Processing of Polish L2 Interlanguage

### Project Overview – What Is Implemented So Far?

At this stage, the project includes:
- `prepare_rag_source.py` that takes the raw LaTeX thesis and prepares it for use in a RAG pipeline.
- `main.py` with:
  - document chunking,
  - vectorization and retrieval,
  - LLM answer generation.

**Next steps:**
- adding a proper source citing from `biblio.bib`,
- a detailed program evaluation,
- a web UI for interactive QA.

### Tools and Components Used

**LaTeX Preprocessing:**
- Python (custom macro replacement, TIPA → IPA conversion)
- Pandoc (LaTeX → Markdown conversion)

**Document Structuring and Chunking:** LangChain (MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter)

**Embeddings:** OpenAI Embeddings API

**Vector Store:** ChromaDB

**Retrieval and Ranking:** Chroma similarity search

**Generation (Answering Questions):** OpenAI LLM (`gpt-4o-mini`)

## Part 1: Preparing Thesis Documents for Retrieval-Augmented Generation

The chatbot relies on RAG to ground its answers in the content of the thesis. Before this can happen, the thesis must be converted into a clean, LLM-friendly format.

### Why Is Preprocessing Needed?

The thesis includes a phonetic analysis of Polish L2 interlanguage, which contains extensive IPA (International Phonetic Alphabet) notation. These IPA symbols were originally written in LaTeX using the TIPA package.

However, most document-conversion tools cannot interpret TIPA macros, leading to broken Unicode characters or empty placeholders in the output.

Since high-quality text representation is crucial for RAG, the TIPA macros must be manually expanded and mapped to proper Unicode IPA symbols before conversion.

### `prepare_rag_source.py`

The script performs a full preprocessing pipeline to ensure the thesis is clean, Unicode-correct, and ready for ingestion by a RAG system.

1. External macro replacement

Expands custom LaTeX macros into plain Unicode characters.

2. TIPA phonetic transcription conversion

Extracts `\textipa{...}` blocks and converts TIPA to clean IPA.

3. LaTeX cleanup

Produces a simplified intermediate `.tex` file without custom commands.

4. Pandoc conversion to Markdown

Generates `main.md` (LLM-friendly, UTF-8 clean, citations resolved) and places the file into `data/final/`.

5. Clean RAG-ready output

The final stage produces two files in `data/final/` that are ready to be consumed directly by a RAG pipeline:
- `biblio.bib` — copied unchanged from the original source.
- `main.md` — the fully cleaned Markdown version of the thesis.

## Part 2: Chunking, Vectorization and Question Answering

Once the thesis has been preprocessed and exported as `main.md` + `biblio.bib`, the next step is to split the document into meaningful chunks, prepare a vector database for RAG and generate answers using an LLM.

### `main.py`

This script implements the RAG pipeline:

1. Load Corpus:

Reads `main.md` and `biblio.bib` from `data/final/` and concatenates them.

2. Markdown-based Document Splitting:

Uses header hierarchy (#, ##, ###, ####) to create structured sections.

Metadata captures the full header path for context relevance.

3. Recursive Chunking:

Chunks each section into smaller pieces (1800 characters, 200 overlap).

Header metadata is prepended to each chunk (and duplicated) to increase its weight during embedding and maintain strong context relevance in academic content.

4. Vector Store Creation:

Creates a Chroma vectorstore using OpenAI embeddings.

Stores chunk embeddings for fast similarity search.

5. RAG-based Question Answering:

Accepts a user question via CLI.

Retrieves the most relevant chunks using similarity search.

Feeds concatenated context to OpenAI LLM (`gpt-4o-mini`) for generating answers.

#### Folder organization

```
RAG_chatQA/
│
├─ data/
│  │
│  ├─ raw/           # Original LaTeX thesis and bibliography (modele.tex, page-de-garde.tex, documentation.tex, biblio.bib)
│  ├─ intermediate/  # Cleaned intermediate LaTeX file with IPA macros replaced (cleaned_ipa.tex)
│  └─ final/         # Final markdown files ready for RAG (main.md, biblio.bib)
│
├─ chroma/           # Chroma vectorstore directory
│
├─ scr/
│  │
│  ├─ prepare_rag_source.py/ # LaTeX preprocessing and conversion
└─ └─ main.py/       # RAG pipeline: chunking, vectorstore, question answering
```

### Installation

1. Clone the repository:

```
git clone git@github.com:agataskrzyniarz1/RAG_chatQA.git
cd RAG_chatQA
```

2. Install Python dependencies:

```
pip install -r requirements.txt
```

3. Install Pandoc for LaTeX → Markdown conversion:

```
sudo apt install pandoc
```

4. Set your OpenAI API key:

```
export OPENAI_API_KEY="your_api_key_here"
```

Alternatively, if the variable is not set, the script will ask you to enter the key interactively at runtime.

### Usage

1. Prepare thesis source:

```
python prepare_rag_source.py
```

2. Ask a question:

```
python main.py "What are the main objectives of the thesis?"
```

### ⚠️ About the Data ⚠️

This repository does not include my full thesis as it is not **yet** published, so the raw content is intentionally omitted for copyright reasons.

The `data/` directory will be uploaded as soon as the thesis is published.


