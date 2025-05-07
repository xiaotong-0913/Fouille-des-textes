from datasets import load_dataset
import os
import random

# Label mapping
label_map = {0: "negative", 1: "neutral", 2: "positive"}

# Number samples per class
nb_per_class = 500
output_root = "corpus"

# Load and shuffle dataset
ds = load_dataset("vincha77/filtered_yelp_restaurant_reviews")["train"]
ds = ds.shuffle(seed=42)

# Initialize counters
class_counts = {0: 0, 1: 0, 2: 0}

# Create output folders
for class_name in label_map.values():
    os.makedirs(os.path.join(output_root, class_name), exist_ok=True)

# Save samples
for item in ds:
    label = item["label"]
    if class_counts[label] >= nb_per_class:
        continue

    label_name = label_map[label]
    count = class_counts[label] + 1
    filename = os.path.join(output_root, label_name, f"{label_name}_{count:04d}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(item["text"].strip())

    class_counts[label] += 1

    if all(c >= nb_per_class for c in class_counts.values()):
        break

print("Corpus generated: 1000 samples per class in 'corpus/'")
