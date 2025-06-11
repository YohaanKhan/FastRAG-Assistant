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
    # Need to add file validation code here
    # Then create two functions, one to convert the image input 
    # into text files and save it, one more to process pdf files to text
    # Next, we also need to feed the same to preprocess and convert into vector chunks,
    # saving it into a database for future reference
    # That is all RAG thingy 

    return ("This is the file type:", file.filename)

