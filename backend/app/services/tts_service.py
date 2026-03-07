class TTSService:
    """Stub TTS service. Will be replaced with Piper/Coqui/Bark/StyleTTS2."""

    async def synthesize(self, text: str) -> bytes:
        raise NotImplementedError("TTS service not yet implemented")
