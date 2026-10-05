import json
import faiss
from sentence_transformers import SentenceTransformer

from rag import ask
print("loaded modules")

model = SentenceTransformer("BAAI/bge-small-en-v1.5")
print("loaded model")
index = faiss.read_index("data/index.faiss")
print("loaded faiss")
with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)
print("loaded chunks")

while True:
    query = input("Question: ")

    if query.lower() == "exit":
        break

    answer = ask(query, model, index, chunks,3)

    print(answer)