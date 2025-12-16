# CBIS-DDSM Mammogram Project

This repository contains code for extracting, organizing, and splitting the CBIS-DDSM mammogram dataset.

---

## 📁 Project Structure

---

## ⚙️ Setup Environment

▶️ How to Run This Project

1️⃣ Clone the Repository

git clone https://github.com/MohitBajpai78271/Calibre_Research.git

cd Calibre_Research

2️⃣ Create Python Environment (Required)
 -> Python 3.10 is required. Python 3.12 may not be supported.
 ```bash
conda create -n visionmamba python=3.10 -y
conda activate visionmamba
```

3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4️⃣ Download Dataset (CBIS-DDSM)

Due to size limitations (>1GB), the dataset is not included in this repository.

1. Download CBIS-DDSM dataset from:
   https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM

2. Place the zip file here:
     data/raw/CBIS-DDSM.zip

5️⃣ Extract Dataset
```bash
python scripts/extract_dataset.py
```
This will create:
data/raw/cbis_ddsm/

6️⃣ Split Dataset (Train / Val / Test)

```bash
python scripts/split_dataset.py
```

7️⃣ Run Experiments (Notebook)
jupyter notebook
Open:notebooks/training.ipynb
Make sure the kernel is set to:
Python (visionmamba)


