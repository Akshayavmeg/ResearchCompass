import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# LLM Configuration
# -----------------------------
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

# -----------------------------
# Tavily Configuration
# -----------------------------
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

# -----------------------------
# ChromaDB Configuration
# -----------------------------
CHROMA_DB_PATH = "vectorstore"

# -----------------------------
# Embedding Model
# -----------------------------
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"