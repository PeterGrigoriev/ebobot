"""Fixtures for E2E Playwright tests against the live FastAPI server."""

from __future__ import annotations

import asyncio
import socket
import threading
import time
from typing import AsyncIterator

import httpx
import pytest
import uvicorn

# ---------------------------------------------------------------------------
# Constants for deterministic mock responses
# ---------------------------------------------------------------------------
OPENING_MESSAGE = "I am T-800. State your query."
STREAM_RESPONSE = "Affirmative. I understand your concern."


# ---------------------------------------------------------------------------
# LLM mock — applied before the server starts
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session", autouse=True)
def mock_llm():
    """Monkey-patch the LLM singleton so no real API calls are made."""
    from app.core.deps import llm_service

    async def mock_generate(messages: list[dict], system_prompt: str) -> str:
        return OPENING_MESSAGE

    async def mock_generate_stream(
        messages: list[dict], system_prompt: str
    ) -> AsyncIterator[str]:
        for word in STREAM_RESPONSE.split():
            yield word + " "
            await asyncio.sleep(0.02)  # simulate slight latency

    llm_service.generate_response = mock_generate
    llm_service.generate_response_stream = mock_generate_stream
    yield
    # No teardown needed — process exits after tests


# ---------------------------------------------------------------------------
# Live server fixture
# ---------------------------------------------------------------------------
def _get_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


@pytest.fixture(scope="session")
def live_server(mock_llm) -> str:
    """Start a real uvicorn server in a background thread and yield its URL."""
    port = _get_free_port()

    config = uvicorn.Config(
        "app.main:app",
        host="127.0.0.1",
        port=port,
        log_level="warning",
    )
    server = uvicorn.Server(config)

    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()

    # Wait for the server to be ready
    deadline = time.monotonic() + 10
    while time.monotonic() < deadline:
        try:
            resp = httpx.get(f"http://127.0.0.1:{port}/api/personas")
            if resp.status_code < 500:
                break
        except httpx.ConnectError:
            pass
        time.sleep(0.1)
    else:
        raise RuntimeError("Live server did not start in time")

    yield f"http://127.0.0.1:{port}"

    server.should_exit = True
    thread.join(timeout=5)


# ---------------------------------------------------------------------------
# Clear sessions between tests
# ---------------------------------------------------------------------------
@pytest.fixture(autouse=True)
def _clear_sessions():
    """Remove all in-memory sessions before each test."""
    from app.core.deps import sessions

    sessions.clear()
    yield
    sessions.clear()


# ---------------------------------------------------------------------------
# Playwright page pointed at the live server
# ---------------------------------------------------------------------------
@pytest.fixture()
def page(live_server: str, page):
    """Override the default pytest-playwright page to set a base URL."""
    page.goto(live_server)
    # Return the page already on the home page
    yield page
