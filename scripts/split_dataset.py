import os
import shutil
import random

SOURCE_DIR = "data/raw/cbis_ddsm"
DEST_DIR = "data/processed"

SPLITS = {"train": 0.7, "val": 0.15, "test": 0.15}

os.makedirs(DEST_DIR, exist_ok=True)

files = os.listdir(SOURCE_DIR)
random.shuffle(files)

start = 0
for split, ratio in SPLITS.items():
    split_dir = os.path.join(DEST_DIR, split)
    os.makedirs(split_dir, exist_ok=True)

    end = start + int(len(files) * ratio)
    for f in files[start:end]:
        shutil.copy(os.path.join(SOURCE_DIR, f), split_dir)

    start = end

print("Dataset split completed!")
