import faiss
from embed import embed

def retrieve(query : str, model, index, chunks: list[str], k : int =3):
    if len(query) == 0:
        raise ValueError("query cant be empty")
    if k<=0:
        raise ValueError("k cant be less than or equal to zero")
    

    query_embeddings=embed([query],model)
    distances,indices=index.search(query_embeddings,k)

    retrieved_chunks=[]
    for indice in indices[0]:
         retrieved_chunks.append(chunks[indice])

    return retrieved_chunks
