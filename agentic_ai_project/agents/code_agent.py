from .base_agent import BaseAgent
from .roles import AgentConfig, AgentRole
from typing import List, Dict

class CodeAgent(BaseAgent):
    def __init__(self, model_name: str, tools: List[str] = None):
        config = AgentConfig(
            role=AgentRole.CODER,
            model_name=model_name,
            system_instruction="You are an expert software engineer. Write clean, efficient, and well-documented code based on user requirements.",
            tools=tools
        )
        super().__init__(config)

    def execute_task(self, task: str) -> str:
        prompt = f"Coding task: {task}\nProvide code in markdown format with explanations."
        return self.send_message(prompt)
