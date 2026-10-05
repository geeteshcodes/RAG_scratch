import faiss

def index(embeddings):
    if embeddings is None:
        raise ValueError("Embeddings cant be empty")
    dimension=embeddings.shape[1]
    faiss_index=faiss.IndexFlatL2(dimension)
    faiss_index.add(embeddings)
    return faiss_index