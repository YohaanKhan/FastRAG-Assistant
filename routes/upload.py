from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from pathlib import Path

router = APIRouter()

class UploadRequest(BaseModel):
    # File Validation Code to be here
    pass 

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)):
    # 1: Validate the uploaded file type (e.g., PDF, DOCX, TXT, PNG, JPG)
    #   - Reject unsupported formats with appropriate HTTP error.

    # 2: Save the uploaded file temporarily to the database for processing.

    # 3: Process the file content:
    #   - For PDFs/DOCX/TXT → extract raw text
    #   - For images → apply OCR to extract readable text

    # 4: Chunk the extracted text into manageable segments
    #   - These chunks will be used for semantic search

    # 5: Generate vector embeddings for the chunks using a local embedding model
    #   - Store these in a vector database (e.g., ChromaDB, FAISS)

    # 6: Optionally, associate metadata (filename, timestamp, user info, tags)

    # 7: Return a success response with relevant upload and indexing info


    return ("This is the file type:", file.filename)




