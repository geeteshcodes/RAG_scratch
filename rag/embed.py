from sentence_transformers import SentenceTransformer

def embed(chunks : list[str],model):
    if len(chunks)<=0:
        raise ValueError("Number of chunks must be greater than zero")
    if model is None:
        raise ValueError("Embedding model cannot be None")
    if not hasattr(model, "encode"):
        raise TypeError("Model must have an encode method")

    embeddings=model.encode(chunks)
    return embeddings

if __name__ == "__main__":
    chunks=["hello this is a test","to check the validity of embed funntions"]
    model=SentenceTransformer("BAAI/bge-small-en-v1.5")
    embeddings=embed(chunks,model)
    print(embeddings.shape)
