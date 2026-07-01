# 🛡️ Cyber Threat Analyzer

An intelligent cyber threat analysis system based on the **MITRE ATT&CK framework**, **Machine Learning**, and **Semantic Search**.

The system automatically analyzes incident descriptions, identifies the most relevant MITRE ATT&CK techniques using vector embeddings, assesses risk, and generates structured recommendations.

---

## 📌 Features

- MITRE ATT&CK knowledge base
- Semantic search using Sentence Transformers
- ChromaDB vector database
- Machine Learning (KMeans clustering)
- Automatic risk assessment
- Recommendation generation
- FastAPI web interface
- Modern dashboard for cyber analysts

---

## 🏗️ Project Architecture

```
User Input
      │
      ▼
Sentence Transformer
      │
      ▼
Embedding Vector
      │
      ▼
ChromaDB
      │
      ▼
Semantic Search
      │
      ▼
Relevant MITRE ATT&CK Techniques
      │
      ▼
Risk Assessment
      │
      ▼
Recommendations
      │
      ▼
Threat Report
```

---

## 📂 Project Structure

```
app/
│
├── api/                # FastAPI application
├── embeddings/         # Embedding generation
├── mitre/              # MITRE ATT&CK parser
├── ml/                 # Machine learning (KMeans)
├── reports/            # Threat report generation
├── vector_db/          # ChromaDB integration
├── export/             # PDF export
└── file_reader/        # File processing (future)

templates/              # HTML templates
static/                 # CSS & JavaScript
data/                   # Generated embeddings and database
```

---

## 🧠 Technologies

- Python 3.12
- FastAPI
- SentenceTransformers
- ChromaDB
- Scikit-learn
- ReportLab
- Jinja2
- HTML/CSS
- MITRE ATT&CK

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/mitre-attack-rag.git
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Build Vector Database

```bash
python -m app.main
```

---

## Run Application

```bash
uvicorn app.api.app:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

## Example Query

```
The attacker dumped credentials from LSASS memory using Mimikatz.
```

The system will

- generate embeddings
- perform semantic search
- identify relevant MITRE ATT&CK techniques
- calculate risk level
- generate recommendations
- display the threat report

---

## Current Functionality

- ✅ MITRE ATT&CK parsing
- ✅ Embedding generation
- ✅ Semantic search
- ✅ ChromaDB integration
- ✅ KMeans clustering
- ✅ Threat report generation
- ✅ FastAPI web interface
- ✅ Dashboard

---

## Planned Features

- PDF/DOCX/TXT analysis
- PDF report export
- Drag & Drop file upload
- Interactive dashboard
- LLM integration (future work)

---

## Author

Sofiia Parfylo

Bachelor Student in Cybersecurity

Sumy State University
