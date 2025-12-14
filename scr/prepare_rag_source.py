import re
import subprocess
import os
import shutil

EXTERNAL_MACROS = {
    r"\texttoptiebar{\textrtaild\textrtailz}": "d͡ʐ",
    r"\texttoptiebar{\textdctzlig}": "d͡ʑ",
    r"\texttoptiebar{t\textrtails}": "t͡ʂ",
    r"\texttoptiebar{\texttctclig}": "t͡ɕ",
    r"\textltailn": "ɲ",
    r"\textctc": "ɕ",
    r"\textctz": "ʑ",
    r"\textrtailz": "ʐ",
    r"\textrtails": "ʂ",
    r"\texttoptiebar{ts}": "t͡s",
    r"\texttoptiebar{dz}": "d͡z",
}

TIPA_MAP = {
    "a": "a",
    "b": "b",
    "d": "d",
    "f": "f",
    "g": "ɡ",
    "j": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "n",
    "p": "p",
    "r": "r",
    "s": "s",
    "t": "t",
    "u": "u",
    "v": "v",
    "w": "w",
    "x": "x",
    "z": "z",
    "ON": "ɔŋ",
    r"\~O\~w": "ɔ̃w̃",
    "E": "ɛ",
    "EN": "ɛŋ",
    r"\~E\~w": "ɛ̃w̃",
    "1": "ɨ",
    "O": "ɔ",
}

VOWELS = "aeɛoɔuɨyãẽõɛ̃ɔ̃"

# === Convert TIPA blocks to IPA characters ===

def replace_external_macros(text):
    for macro, rep in EXTERNAL_MACROS.items():
        text = text.replace(macro, rep)
    return text

# If "i" is before a vowel -> change for "j" (according to Polish pronunciation)
def contextual_i_to_j(text):
    result = []
    for i, ch in enumerate(text):
        if ch == "i" and i + 1 < len(text) and text[i+1] in VOWELS:
            result.append("j")
        else:
            result.append(ch)
    return "".join(result)


def replace_tipa_in_block(tipa_text):
    keys = sorted(TIPA_MAP.keys(), key=len, reverse=True)
    for key in keys:
        tipa_text = tipa_text.replace(key, TIPA_MAP[key])
    return contextual_i_to_j(tipa_text)


def process_tipa_blocks(text):
    pattern = r"(\\textipa\{([^}]*)\})"

    def repl(match):
        inner = match.group(2)
        return replace_tipa_in_block(inner)

    return re.sub(pattern, repl, text)

# === PANDOC : convert .tex to .md file ===

def run_pandoc(input_tex, output_md, bibfile, cwd):
    cmd = [
        "pandoc",
        input_tex,
        "--from=latex",
        "--to=markdown",
        "--output", output_md,
        "--citeproc",
        "--bibliography=" + bibfile,
        "--standalone",
        "--wrap=none",
        "--top-level-division=chapter"
    ]

    print(f"\nRunning Pandoc in folder: {cwd}")
    print(" ".join(cmd))

    subprocess.run(cmd, cwd=cwd, check=True)

# === Main ===

def main():
    # Determine folders
    script_dir = os.path.dirname(os.path.abspath(__file__))

    raw_dir = os.path.abspath(os.path.join(script_dir, "..", "data", "raw"))
    inter_dir = os.path.abspath(os.path.join(script_dir, "..", "data", "intermediate"))
    final_dir = os.path.abspath(os.path.join(script_dir, "..", "data", "final"))

    os.makedirs(inter_dir, exist_ok=True)
    os.makedirs(final_dir, exist_ok=True)

    # Filenames
    input_tex = "modele.tex"
    cleaned_tex = "cleaned_ipa.tex"
    output_md = "main_with_noise.md"
    bib = "biblio.bib"

    input_tex_path = os.path.join(raw_dir, input_tex)

    # Load original LaTeX
    with open(input_tex_path, "r", encoding="utf-8") as f:
        text = f.read()

    # External macros
    text = replace_external_macros(text)

    # Replace TIPA blocks
    text = process_tipa_blocks(text)

    # Write cleaned LaTeX to intermediate/
    cleaned_path = os.path.join(inter_dir, cleaned_tex)
    with open(cleaned_path, "w", encoding="utf-8") as f:
        f.write(text)

    # Copy cleaned file back to raw/
    cleaned_for_pandoc = os.path.join(raw_dir, cleaned_tex)
    shutil.copy(cleaned_path, cleaned_for_pandoc)

    # Run Pandoc, output directly to final/
    run_pandoc(
        input_tex=cleaned_tex,
        output_md=os.path.join(inter_dir, output_md),
        bibfile=bib,
        cwd=raw_dir
    )

    # Copy bibliography to final/
    shutil.copy(os.path.join(raw_dir, bib), os.path.join(final_dir, bib))

    print("\nFiles generated:")
    print(f"- cleaned LaTeX:   {cleaned_path}")
    print(f"- Markdown:        {os.path.join(inter_dir, output_md)}")
    print(f"- Bibliography:    {os.path.join(final_dir, bib)}")


if __name__ == "__main__":
    main()
