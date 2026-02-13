from .base_agent import BaseAgent
from .roles import AgentConfig, AgentRole
from typing import List, Dict

class ResearchAgent(BaseAgent):
    def __init__(self, model_name: str, tools: List[str] = None):
        config = AgentConfig(
            role=AgentRole.RESEARCHER,
            model_name=model_name,
            system_instruction="You are a research agent. Use provided tools to gather information and synthesize comprehensive answers.",
            tools=tools
        )
        super().__init__(config)

    def execute_task(self, task: str) -> str:
        prompt = f"Research task: {task}\nUse your tools to find the answer."
        return self.send_message(prompt)
