import anthropic
import getpass
import json
import os

# Ask for API key
api_key = getpass.getpass("Enter your Anthropic API key: ")

client = anthropic.Anthropic(api_key=api_key)

# Load thesis text
thesis_path = "../data/final/main.md"
biblio_path = "../data/final/biblio.bib"

def load_corpus(thesis_path: str) -> str:
    with open(thesis_path, "r", encoding="utf-8") as f:
        return f.read()
    
thesis_text = load_corpus(thesis_path)
biblio_text = load_corpus(biblio_path)

# Prompt 1
PROMPT_1 = f"""
Generate approximately 15 high-level, conceptual questions based on the document below (master's thesis), along with their answers.

The questions should:
- focus on big-picture aspects of the thesis:
  - research goals and motivations
  - theoretical background
  - methodology
  - data used in the study
  - overall findings and key conclusions
  - limitations and future work
- DO NOT ask about low-level details.

The answers must:
- include citing if needed: find appropriate tags in the bibliography file and extract the author and year -> use citations in a form (Author, Year) 
- be written as complete, grammatically correct sentences
- vary in length depending on the question
- use bullet points, numbered lists, or tables if suitable

Formatting requirements:
- Produce strictly valid JSON
- Output a list of objects, each with:
  - "question"
  - "ground_truth"

The document:

{thesis_text}

The bibliography (.bib format):

{biblio_text}
"""


# Prompt 2
PROMPT_2 = f"""
Generate approximately 50 questions based on the document below (master's thesis) along with their answers. 

- Each answer must be written as a complete, grammatically correct sentence, even if it is short.
- The answers should vary in length and format depending on the question.
- Don't forget about bullet points, numbered lists, or tables if suitable.
- Make sure every question is meaningful and answerable based on the document.
- Include citing if needed: find appropriate tags in the bibliography file and extract the author and year -> use citations in a form (Author, Year)
- Generate the output strictly in valid JSON format as a list of objects, where each object has two fields: "question" and "ground_truth".

The document:

{thesis_text}

The bibliography (.bib format):

{biblio_text}
"""

# Call Claude LLM
message = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=20000,
    temperature=1,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": PROMPT_2
                }
            ]
        }
    ]
)

# Extract clean JSON from response
raw_text = message.content[0].text
clean_text = raw_text.strip().strip("```").replace("json\n", "")
data = json.loads(clean_text)

#print(data)

# Save file
output_dir = "../data/eval"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "eval_data_50.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"\nSaved evaluation dataset to: {output_path}")