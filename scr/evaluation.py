import json
import os
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)
from ragas.embeddings import OpenAIEmbeddings
from openai import OpenAI
from main import get_rag_answer

# Load evaluation file
with open("../data/eval/eval_data_final.json", "r", encoding="utf-8") as f:
    qa_pairs = json.load(f)


class RagasEmbeddingWrapper:
    def __init__(self, embeddings):
        self.embeddings = embeddings

    def embed_query(self, text: str):
        return self.embeddings.embed_text(text)

    def embed_documents(self, texts):
        return self.embeddings.embed_texts(texts)


# Embeddings
client = OpenAI()
base_embeddings = OpenAIEmbeddings(client=client)

embeddings = RagasEmbeddingWrapper(base_embeddings)


questions = []
ground_truths = []
responses = []
contexts = []

# Run RAG for each question
for item in qa_pairs:
    q = item["question"]
    gt = item["ground_truth"]

    rag_answer, _, context_for_eval = get_rag_answer(q)

    questions.append(q)
    ground_truths.append(gt)
    responses.append(rag_answer)
    contexts.append(context_for_eval)

# Build RAGAS dataset
ragas_dataset = Dataset.from_dict({
    "question": questions,
    "answer": responses,
    "contexts": contexts,
    "ground_truth": ground_truths,
})

# Evaluate
results = evaluate(
    ragas_dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall,
    ],
    embeddings=embeddings,
)

df = results.to_pandas()

# Save CSV
output_dir = "../data/eval"
os.makedirs(output_dir, exist_ok=True)

df.to_csv(f"{output_dir}/ragas_evaluation_results_final.csv", index=False)

print(f"Saved: {output_dir}/ragas_evaluation_results_final.csv")
