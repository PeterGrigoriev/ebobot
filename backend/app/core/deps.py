from __future__ import annotations

from typing import TYPE_CHECKING

from app.services.llm_service import LLMService

if TYPE_CHECKING:
    from app.models.session import Session

# Shared singletons
llm_service = LLMService()
sessions: dict[str, Session] = {}
