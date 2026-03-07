from __future__ import annotations

import json

from fastapi import APIRouter, HTTPException
from starlette.responses import StreamingResponse

from app.core.deps import llm_service, sessions
from app.models.chat import ChatRequest, Message
from app.models.session import SessionStatus

router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.post("/{session_id}")
async def chat(session_id: str, body: ChatRequest):
    session = sessions.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if session.status != SessionStatus.ACTIVE:
        raise HTTPException(status_code=400, detail="Session is not active")

    session.messages.append(Message(role="user", content=body.message))

    api_messages = [{"role": m.role, "content": m.content} for m in session.messages]

    async def event_stream():
        full_response = ""
        try:
            async for token in llm_service.generate_response_stream(
                messages=api_messages,
                system_prompt=session.system_prompt or "",
            ):
                full_response += token
                yield f"event: token\ndata: {json.dumps(token)}\n\n"
        except Exception as e:
            yield f"event: error\ndata: {json.dumps(str(e))}\n\n"
            return
        session.messages.append(Message(role="assistant", content=full_response))
        yield "event: done\ndata: {}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
