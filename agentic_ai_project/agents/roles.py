from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional

class AgentRole(Enum):
    RESEARCHER = auto()
    CODER = auto()
    ORCHESTRATOR = auto()
    CRITIC = auto()

@dataclass
class AgentConfig:
    role: AgentRole
    model_name: str
    temperature: float = 0.7
    system_instruction: Optional[str] = None
    tools: List[str] = None
