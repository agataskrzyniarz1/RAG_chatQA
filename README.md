# RAG-Thesis-Chatbot

## Part 1: Preparing Thesis Documents for Retrieval-Augmented Generation

This repository contains the first stage of a larger RAG project. The end goal is to build an interactive question-answering chatbot capable of answering questions about my master thesis:

> Performance Evaluation of Tools for Automatic Processing of Polish L2 Interlanguage

The chatbot will rely on RAG to ground its answers in the content of the thesis. Before this can happen, the thesis must be converted into a clean, LLM-friendly format. This repository provides the preprocessing script responsible for that task.

### Project Overview – What Is Implemented So Far?

At this stage, the project includes:
- A Python script (`prepare_rag_source.py`) that takes the raw LaTeX thesis and prepares it for use in a RAG pipeline.
- A structured data folder where:
  - raw LaTeX files are placed,
  - intermediate cleaned data is generated,
  - final Markdown + bibliography are produced.

Future stages will include:
- document chunking,
- vectorization and retrieval,
- LLM answer generation,
- a web UI for interactive QA.

### Why Is Preprocessing Needed?

The thesis includes a phonetic analysis of Polish L2 interlanguage, which contains extensive IPA (International Phonetic Alphabet) notation. These IPA symbols were originally written in LaTeX using the TIPA package.

However, most document-conversion tools (including Pandoc) cannot interpret TIPA macros, leading to broken Unicode characters or empty placeholders in the output.

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

#### Folder organization

```
data/
│
├── raw/             # Original LaTeX source (modele.tex, page-de-garde.tex, documentation.tex, biblio.bib)
├── intermediate/    # Cleaned intermediate file (cleaned_ipa.tex)
└── final/           # Final RAG-ready files (main.md, biblio.bib)
```

### Requirements

- Python 3.9+
- Pandoc installed (required for LaTeX → Markdown conversion)

```
sudo apt update
sudo apt install pandoc
```

#### Python dependencies

The script uses only the standard library:
- re
- subprocess
- os
- shutil

No external packages required.

### Usage

Run the script from the project root:

```
python prepare_rag_source.py
```

### About the Data

This repository does not include my full thesis as it is not **yet** published, so the raw content is intentionally omitted for copyright reasons.

The `data/` directory will be uploaded as soon as the thesis is published.
