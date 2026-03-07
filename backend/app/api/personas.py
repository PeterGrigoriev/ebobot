from pathlib import Path

import yaml
from fastapi import APIRouter, HTTPException

from app.models.persona import Persona, PersonaConfig

router = APIRouter(prefix="/api/personas", tags=["personas"])

PERSONAS_DIR = Path(__file__).parent.parent / "personas"


def _load_personas() -> list[PersonaConfig]:
    personas = []
    if PERSONAS_DIR.exists():
        for path in sorted(PERSONAS_DIR.glob("*.yaml")):
            with open(path) as f:
                data = yaml.safe_load(f)
            config = data.get("persona", data)
            personas.append(PersonaConfig(**config))
    return personas


@router.get("", response_model=list[Persona])
async def list_personas():
    configs = _load_personas()
    return [
        Persona(
            id=p.id,
            name=p.name,
            source=p.source,
            language_primary=p.language_primary,
            crisis_type=p.character.crisis_type,
        )
        for p in configs
    ]


@router.get("/{persona_id}", response_model=PersonaConfig)
async def get_persona(persona_id: str):
    for p in _load_personas():
        if p.id == persona_id:
            return p
    raise HTTPException(status_code=404, detail="Persona not found")
