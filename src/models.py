from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    question: str
    topic: Optional[str] = None
    level: Optional[str] = None


class ChatResponse(BaseModel):
    answer: str
