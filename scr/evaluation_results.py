import os
import pandas as pd
import matplotlib.pyplot as plt

# Paths
input_csv = "../data/eval/ragas_evaluation_results_final.csv"
output_dir = "../img"

os.makedirs(output_dir, exist_ok=True)

# Load data
df = pd.read_csv(input_csv)

metrics = [
    "faithfulness",
    "answer_relevancy",
    "context_precision",
    "context_recall",
]

x = range(len(df))

# === BOXPLOT ===

plt.figure(figsize=(10, 6))
plt.boxplot(
    [df[m] for m in metrics],
    tick_labels=metrics,
    showfliers=True
)
plt.ylabel("Score")
plt.title("RAG Evaluation")
plt.ylim(0, 1.05)
plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "ragas_boxplot.png"), dpi=300)
plt.close()

print(f"Saved boxplot in {output_dir}.")

# === LINE PLOTS ===

for metric in metrics:
    plt.figure(figsize=(10, 4))
    plt.plot(x, df[metric], marker="o", linestyle="-")
    plt.xlabel("Question index")
    plt.ylabel(metric)
    plt.title(f"{metric}")
    plt.ylim(0, 1.05)
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{metric}.png"), dpi=300)
    plt.close()

    print(f"Saved line plots in {output_dir}.")