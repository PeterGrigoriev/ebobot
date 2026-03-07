class STTService:
    """Stub STT service. Will be replaced with Whisper."""

    async def transcribe(self, audio: bytes) -> str:
        raise NotImplementedError("STT service not yet implemented")
