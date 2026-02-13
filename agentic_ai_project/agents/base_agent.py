import os
import google.generativeai as genai
from abc import ABC, abstractmethod
from typing import List, Any, Dict
from .roles import AgentConfig

class BaseAgent(ABC):
    def __init__(self, config: AgentConfig):
        self.config = config
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        
        genai.configure(api_key=self.api_key)
        
        self.model = genai.GenerativeModel(
            model_name=config.model_name,
            system_instruction=config.system_instruction,
            tools=config.tools
        )
        self.chat = self.model.start_chat()
        self.history = []

    def send_message(self, message: str) -> str:
        """Sends a message to the agent and returns the response."""
        try:
            response = self.chat.send_message(message)
            self.history.append({"role": "user", "parts": [message]})
            self.history.append({"role": "model", "parts": [response.text]})
            return response.text
        except Exception as e:
            return f"Error communicating with Gemini: {e}"

    @abstractmethod
    def execute_task(self, task: str) -> str:
        """Abstract method for agents to implement specific task logic."""
        pass
