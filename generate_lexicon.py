from pathlib import Path
from collections import Counter
import re

corpus_dir = Path("corpus")  # Path to your corpus directory
all_words = []

# Collect all words from text files
for file in corpus_dir.rglob("*.txt"):
    if file.name.startswith("."):
        continue
    text = file.read_text(encoding="utf-8")
    words = re.findall(r"\b\w+\b", text.lower())  # Extract words using regex
    all_words.extend(words)

# Count word frequencies
counter = Counter(all_words)

# Filter out words that appear only once
filtered_words = [word for word, freq in counter.items() if freq > 1]

# Write the lexicon to a file
with open("lexique.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(filtered_words)))

print(f"Lexicon generated with {len(filtered_words)} words.")
