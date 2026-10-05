def chunk(document: str, chunk_size: int = 1000, overlap: int = 100) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if len(document) == 0:
        raise ValueError("Document text cannot be empty. Check document or document parser")
    chunks = []
    start = 0
    while start < len(document):
        end = start + chunk_size
        if end >= len(document):
            chunks.append(document[start:len(document)])
            break
        chunks.append(document[start:end])
        start = start + chunk_size - overlap
    return chunks

if __name__ == "__main__":
    chunks = chunk("This is some test", 4, 2)
    print(chunks)
    for chunk in chunks:
        print(len(chunk))



