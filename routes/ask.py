from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal, Optional

router = APIRouter()

# Request Schema
class AskRequest(BaseModel):
    topic: str
    subtopics: Optional[str]
    type: Literal["Question_Bank"]
    subject: str
    format: Literal["Paragraph", "Bulletin", "Q&A", "Notes", "Summary"]
    marks: Literal[2, 5, 10]

@router.post("/ask")
async def ask_question(request: AskRequest):
    # We first feed the request to create_prompt function to create a well engineered prompt
    # Then we feed the prompt from the above call to the llm
    # We take the response and return the answer
    return("The answer to the above question is something.")





