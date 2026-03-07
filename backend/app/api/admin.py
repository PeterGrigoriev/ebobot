from fastapi import APIRouter

from app.core.state_machine import InstallationState, StateMachine

router = APIRouter(prefix="/api/admin", tags=["admin"])

# Global state machine instance
state_machine = StateMachine()


@router.get("/status")
async def get_status():
    return {
        "state": state_machine.state.value,
        "available_transitions": [
            s.value for s in InstallationState if state_machine.can_transition(s)
        ],
    }


@router.get("/sessions")
async def list_sessions():
    # Stub — will be wired to session store
    return {"sessions": []}
