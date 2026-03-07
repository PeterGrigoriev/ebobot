from __future__ import annotations

from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str
