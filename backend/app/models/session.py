from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

from app.models.chat import Message


class SessionStatus(str, Enum):
    ACTIVE = "active"
    ENDED = "ended"


class SessionCreate(BaseModel):
    persona_id: str


class Session(BaseModel):
    id: str
    persona_id: str
    status: SessionStatus = SessionStatus.ACTIVE
    started_at: datetime = Field(default_factory=datetime.utcnow)
    ended_at: Optional[datetime] = None
    duration_seconds: Optional[float] = None
    termination_type: Optional[str] = None
    language: Optional[str] = None
    system_prompt: Optional[str] = None
    messages: List[Message] = []
