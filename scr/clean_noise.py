import re
import json

# Paths
main_with_noise_path = "../data/intermediate/main_with_noise.md"

# === Load corpus ===

def load_corpus(main_with_noise_path: str) -> str:
    """Load main.md as corpus."""
    with open(main_with_noise_path, "r", encoding="utf-8") as f:
        return f.read()

corpus_text = load_corpus(main_with_noise_path)

# == Extract noise ==

def extract_curly_blocks(text: str):
    pattern = re.compile(r"\{(?!\n)[^}]+\}")
    return list(set(pattern.findall(text)))

def extract_internal_links(text: str):
    pattern = re.compile(r"\[[^\]]*\]\(#.*?\)")
    return list(set(pattern.findall(text)))

def extract_images_with_attrs(text: str):
    pattern = re.compile(r"!\[[^\]]*\]\([^)]+\)(?:\{[^}]+\}|\([^)]+\))?")
    return list(set(pattern.findall(text)))

def extract_parenthesized_refs(text: str):
    pattern = re.compile(r"\(#.*?\)")
    return list(set(pattern.findall(text)))

def extract_dollar_blocks(text: str):
    pattern = re.compile(r"\$\$.*\$\$")
    return list(set(pattern.findall(text)))

def extract_footnotes(text: str):
    pattern = re.compile(r"\[\^[0-9][0-9]?\]")
    return list(set(pattern.findall(text)))

def extract_square_bracket_labels(text: str):
    pattern = re.compile(r"\\\[(?:fig|app):[^\]]+\\\]")
    return list(set(pattern.findall(text)))


def extract_all_noise_patterns(text: str):
    noise = {
        "curly_blocks": extract_curly_blocks(text),
        "internal_links": extract_internal_links(text),
        "image_blocks": extract_images_with_attrs(text),
        "parenthesized_refs": extract_parenthesized_refs(text),
        "dollar_blocks": extract_dollar_blocks(text),
        "footnotes": extract_footnotes(text),
        "square_bracket_labels": extract_square_bracket_labels(text),
    }
    return noise

# Extract noise patterns
noise = extract_all_noise_patterns(corpus_text)

# Save noise inventory to file
corpus_noise_path = "../data/intermediate/corpus_noise_inventory.json"

with open(corpus_noise_path, "w", encoding="utf-8") as f:
    json.dump(noise, f, indent=2, ensure_ascii=False)

print(f"Saved corpus noise inventory to: {corpus_noise_path}")

# === Remove noise ===

def flatten_noise_inventory(noise_dict):
    all_noise = []
    for values in noise_dict.values():
        all_noise.extend(values)
    return sorted(set(all_noise), key=len, reverse=True)

def remove_noise_from_text(text: str, noise_list: list[str]) -> str:
    for noise in noise_list:
        text = text.replace(noise, "")
    return text

# Load noise inventory from file
with open(corpus_noise_path, "r", encoding="utf-8") as f:
    noise_inventory = json.load(f)

# Flatten and clean the text
noise_list = flatten_noise_inventory(noise_inventory)
clean_text = remove_noise_from_text(corpus_text, noise_list)

# Save cleaned text
clean_path = "../data/final/main.md"

with open(clean_path, "w", encoding="utf-8") as f:
    f.write(clean_text)

print(f"Saved cleaned corpus to: {clean_path}")