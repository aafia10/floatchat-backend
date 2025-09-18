# src/build_chroma.py
import chromadb
from sentence_transformers import SentenceTransformer
from extract_access import load_access_data

DB_PATH = r"data\ARGO_DB_2004.accdb"
BATCH_SIZE = 500  # process in chunks

def build_chroma():
    client = chromadb.PersistentClient(path="./chroma_store")
    collection = client.get_or_create_collection("argo_data")

    print("📥 Loading data from Access DB...")
    docs = load_access_data(DB_PATH, limit_per_table=5000)  # adjustable

    print(f"✅ Loaded {len(docs)} rows. Now generating embeddings...")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    for i in range(0, len(docs), BATCH_SIZE):
        batch = docs[i:i+BATCH_SIZE]
        texts = [d["text"] for d in batch]
        ids = [d["id"] for d in batch]

        embeddings = model.encode(texts, show_progress_bar=True).tolist()

        collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=ids,
        )
        print(f"✔️ Stored batch {i//BATCH_SIZE + 1} "
              f"({len(batch)} docs) in ChromaDB")

    print("🎉 All data stored successfully in ChromaDB!")


if __name__ == "__main__":
    build_chroma()
