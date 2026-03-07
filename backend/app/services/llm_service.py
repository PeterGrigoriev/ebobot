from __future__ import annotations

import os
from typing import AsyncIterator

from anthropic import AsyncAnthropic


class LLMService:
    """LLM service wrapping the Anthropic API. Designed to be swappable with a local model later."""

    def __init__(self) -> None:
        self.client = AsyncAnthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))
        self.model = "claude-sonnet-4-20250514"

    async def generate_response(
        self, messages: list[dict], system_prompt: str
    ) -> str:
        response = await self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=system_prompt,
            messages=messages,
        )
        return response.content[0].text

    async def generate_response_stream(
        self, messages: list[dict], system_prompt: str
    ) -> AsyncIterator[str]:
        async with self.client.messages.stream(
            model=self.model,
            max_tokens=1024,
            system=system_prompt,
            messages=messages,
        ) as stream:
            async for text in stream.text_stream:
                yield text
