from typing import List, Optional

from pydantic import BaseModel


class VoiceEffect(BaseModel):
    type: str
    intensity: Optional[float] = None
    cutoff: Optional[int] = None


class VoiceConfig(BaseModel):
    tts_model: str = ""
    pitch: int = 0
    speed: float = 1.0
    style: str = ""
    effects: List[VoiceEffect] = []


class BehaviorConfig(BaseModel):
    patience_threshold: float = 0.5
    volatility: float = 0.5
    trust_curve: str = "moderate"
    early_termination_probability: float = 0.2


class DialogueConfig(BaseModel):
    required_phases: List[str] = [
        "establishing_contact",
        "initial_request",
        "closing",
    ]
    optional_phases: List[str] = []
    custom_lines: dict = {}


class VisualsConfig(BaseModel):
    avatar: str = ""
    avatar_animation: str = ""
    color_scheme: str = ""


class PersonaCharacter(BaseModel):
    backstory: str = ""
    crisis_type: str = ""
    personality_traits: List[str] = []


class PersonaConfig(BaseModel):
    """Full persona configuration matching the YAML schema."""

    id: str
    name: str
    source: str = ""
    language_primary: str = "ru"
    character: PersonaCharacter = PersonaCharacter()
    behavior: BehaviorConfig = BehaviorConfig()
    dialogue: DialogueConfig = DialogueConfig()
    voice: VoiceConfig = VoiceConfig()
    visuals: VisualsConfig = VisualsConfig()


class Persona(BaseModel):
    """Persona summary returned by API."""

    id: str
    name: str
    source: str
    language_primary: str
    crisis_type: str
