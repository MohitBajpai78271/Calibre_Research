import zipfile
import os

ZIP_PATH = "data/raw/CBIS-DDSM.zip"
EXTRACT_PATH = "data/raw/cbis_ddsm"

os.makedirs(EXTRACT_PATH, exist_ok=True)

with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
    zip_ref.extractall(EXTRACT_PATH)

print("Dataset extracted successfully!")
