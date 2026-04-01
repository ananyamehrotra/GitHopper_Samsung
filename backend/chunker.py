def chunk_code(files, max_chars=3000):
    """
    Chunks code files logic-safely so Bedrock token limits aren't hit.
    """
    chunks = []
    
    for file in files:
        content = file["content"]
        path = file["path"]
        lang = file["language"]
        
        # Basic chunking: split by character limit.
        # A more advanced chunker could split by functions/classes.
        file_len = len(content)
        
        # If the file is very small, we keep it as one chunk entirely
        if file_len <= max_chars:
            chunks.append({
                "file": path,
                "language": lang,
                "code": content,
                "chunk_index": 0,
                "total_chunks": 1
            })
            continue
            
        # If larger, we slice it
        total_chunks = (file_len // max_chars) + (1 if file_len % max_chars > 0 else 0)
        
        for i in range(total_chunks):
            start_idx = i * max_chars
            end_idx = min(start_idx + max_chars, file_len)
            chunk_text = content[start_idx:end_idx]
            
            chunks.append({
                "file": path,
                "language": lang,
                "code": chunk_text,
                "chunk_index": i,
                "total_chunks": total_chunks
            })
            
    return chunks

# Test the pipeline if executed directly
if __name__ == "__main__":
    print("Testing Chunking Logic...")
    sample_files = [{
        "path": "test.txt",
        "language": "txt",
        "content": "A" * 3500
    }]
    
    chunks = chunk_code(sample_files, max_chars=1000)
    print(f"Created {len(chunks)} chunks.")
    if chunks:
        print(f"First chunk length: {len(chunks[0]['code'])}")
        print(f"Last chunk length: {len(chunks[-1]['code'])}")
