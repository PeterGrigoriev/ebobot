from enum import Enum
from typing import Dict, List


class InstallationState(str, Enum):
    ATTRACT = "attract"
    RINGING = "ringing"
    CALL_ACTIVE = "call_active"
    CALL_ENDED = "call_ended"
    COOLDOWN = "cooldown"


# Valid state transitions
_TRANSITIONS: Dict[InstallationState, List[InstallationState]] = {
    InstallationState.ATTRACT: [InstallationState.RINGING],
    InstallationState.RINGING: [InstallationState.CALL_ACTIVE, InstallationState.ATTRACT],
    InstallationState.CALL_ACTIVE: [InstallationState.CALL_ENDED],
    InstallationState.CALL_ENDED: [InstallationState.COOLDOWN],
    InstallationState.COOLDOWN: [InstallationState.ATTRACT],
}


class StateMachine:
    def __init__(self) -> None:
        self.state = InstallationState.ATTRACT

    def can_transition(self, target: InstallationState) -> bool:
        return target in _TRANSITIONS.get(self.state, [])

    def transition(self, target: InstallationState) -> InstallationState:
        if not self.can_transition(target):
            raise ValueError(
                f"Invalid transition: {self.state.value} -> {target.value}"
            )
        self.state = target
        return self.state
