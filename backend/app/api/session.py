from __future__ import annotations

import uuid
from datetime import datetime

from fastapi import APIRouter, HTTPException

from app.api.personas import _load_personas
from app.core.deps import llm_service, sessions
from app.models.chat import Message
from app.models.session import Session, SessionCreate, SessionStatus
from app.services.prompt_builder import build_system_prompt

router = APIRouter(prefix="/api/session", tags=["session"])


@router.post("/start")
async def start_session(body: SessionCreate):
    # Find persona
    persona = None
    for p in _load_personas():
        if p.id == body.persona_id:
            persona = p
            break
    if not persona:
        raise HTTPException(status_code=404, detail="Persona not found")

    system_prompt = build_system_prompt(persona)

    session = Session(
        id=str(uuid.uuid4()),
        persona_id=body.persona_id,
        system_prompt=system_prompt,
    )

    # Generate opening message
    opening = await llm_service.generate_response(
        messages=[{"role": "user", "content": "(The phone rings. You pick up and speak first.)"}],
        system_prompt=system_prompt,
    )
    session.messages.append(Message(role="assistant", content=opening))

    sessions[session.id] = session
    return {
        "session": session.model_dump(),
        "opening_message": opening,
    }


@router.post("/end/{session_id}", response_model=Session)
async def end_session(session_id: str):
    session = sessions.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    session.status = SessionStatus.ENDED
    session.ended_at = datetime.utcnow()
    if session.started_at:
        session.duration_seconds = (
            session.ended_at - session.started_at
        ).total_seconds()
    return session


@router.get("/{session_id}", response_model=Session)
async def get_session(session_id: str):
    session = sessions.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session
