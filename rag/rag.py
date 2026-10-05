from chunk import chunk
from embed import embed
from index import index as create_index
import faiss
from sentence_transformers import SentenceTransformer
import json
from extract import extract
from retrieve import retrieve
from generate import generate
from prompt import prompt as make_prompt


def build_rag(document_path, embedding_model,chunk_size=1000,overlap=100):

    # extract text
    document = extract(document_path)

    # make chunks
    chunks = chunk(document,chunk_size,overlap)

    # create embeddings
    embeddings = embed(chunks, embedding_model)

    # create faiss index
    faiss_index = create_index(embeddings)

    # save index
    faiss.write_index(faiss_index, "data/index.faiss")

    # save chunks
    with open("data/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

def ask(query,model,index,chunks,k=3):

    #retrive the chunks
    retrieved_chunks=retrieve(query,model,index,chunks,k)

    #create prompt
    prompt=make_prompt(query,retrieved_chunks)

    #get llm response
    response=generate(prompt)

    return response


if __name__=="__main__":
    model=SentenceTransformer("BAAI/bge-small-en-v1.5")
    build_rag("C:/geetesh/aimldl/projects/nyc/data/attention-is-all-you-need-Paper.pdf",model,5000,1000)
    
