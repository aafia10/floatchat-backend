import os
import requests
import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("PERPLEXITY_API_KEY")
MODEL_NAME = os.getenv("PERPLEXITY_MODEL", "sonar")  # default valid model

# Init Chroma
client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection("argo_data")

# Embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def query_perplexity(prompt: str) -> str:
    """Send query to Perplexity API"""
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
    except requests.exceptions.Timeout:
        return "⏱️ Perplexity API request timed out."
    except Exception as e:
        return f"❌ Error calling Perplexity API: {e}"

    if resp.status_code != 200:
        # show error message
        try:
            err_json = resp.json()
        except:
            err_json = resp.text
        return f"❌ Perplexity API error ({resp.status_code}): {err_json}"

    # assume structure has choices → message → content
    try:
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Unexpected response format: {resp.text}"


def rag_query(user_query: str, top_k: int = 5) -> str:
    """Perform RAG query using ChromaDB + Perplexity"""
    # Check for API key
    if not API_KEY:
        return "⚠️ Perplexity API key not set. Please add `PERPLEXITY_API_KEY` to .env."

    if collection.count() == 0:
        return "⚠️ No documents found in ChromaDB. Please run build_chroma.py first."

    # Create embedding for query
    q_emb = embedder.encode([user_query]).tolist()[0]

    # Search in Chroma
    results = collection.query(query_embeddings=[q_emb], n_results=top_k)

    if not results or not results.get("documents"):
        return "⚠️ No relevant documents found."

    retrieved_docs = [doc for doc in results["documents"][0] if doc.strip()]
    if not retrieved_docs:
        return "⚠️ Retrieved docs are empty."

    # Build final prompt
    context = "\n".join(retrieved_docs)
    final_prompt = f"Context:\n{context}\n\nQuestion: {user_query}\nAnswer:"

    return query_perplexity(final_prompt)


if __name__ == "__main__":
    q = input("Enter your question: ")
    print("🤖 Answer:", rag_query(q))
