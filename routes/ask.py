from fastapi import APIRouter, UploadFile, File, Form
from pydantic import BaseModel
from typing import Literal, Optional

router = APIRouter()

# ✅ Request Schema
class AskRequest(BaseModel):
    topic: str
    subtopics: Optional[str] = None
    type: Literal["Question_Bank"]  
    subject: str
    format: Literal["Paragraph", "Bulletin", "Q&A", "Notes", "Summary"]
    marks: Literal[2, 5, 10]


# ✅ Ask Text-Based Question
@router.post("/ask-question")
async def ask_question(request: AskRequest):
    # 1. Feed request to create_prompt()
    # 2. Pass to LLM (local or remote)
    # 3. Return the answer
    return {"answer": "🧠 Mocked answer for text-based question"}


# ✅ Ask with Image and Context
@router.post("/ask-with-image")
async def ask_with_image(
    image: UploadFile = File(...),
    prompt: str = Form(...)
):
    # 1. OCR image → extract text
    # 2. Combine with prompt
    # 3. Send to LLM
    return {"answer": "🧠 Mocked answer for image + prompt"}


# ✅ Ask using RAG pipeline
@router.post("/ask-with-rag")
async def ask_with_rag(
    question: str = Form(...),
    file_id: Optional[str] = Form(None)  
):
    # 1. Embed the question
    # 2. Retrieve top-K chunks from ChromaDB or FAISS
    # 3. Build a prompt with context + question
    # 4. Send to local LLM
    return {"answer": "🧠 Mocked RAG-based answer"}



