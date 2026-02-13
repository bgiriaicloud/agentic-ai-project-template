import unittest
from unittest.mock import MagicMock, patch
from agentic_ai_project.agents.research_agent import ResearchAgent
from agentic_ai_project.agents.roles import AgentConfig

class TestResearchAgent(unittest.TestCase):
    @patch('agentic_ai_project.agents.base_agent.genai.GenerativeModel')
    @patch('agentic_ai_project.agents.base_agent.genai.configure')
    @patch('os.getenv')
    def test_research_agent_initialization(self, mock_getenv, mock_configure, mock_model):
        mock_getenv.return_value = "fake_key"
        agent = ResearchAgent(model_name="gemini-1.5-pro")
        
        self.assertIsNotNone(agent)
        mock_configure.assert_called_with(api_key="fake_key")
        mock_model.assert_called()

    @patch('agentic_ai_project.agents.base_agent.genai.GenerativeModel')
    @patch('os.getenv')
    def test_execute_task(self, mock_getenv, mock_model):
        mock_getenv.return_value = "fake_key"
        
        # Mock the chat session and response
        mock_chat = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Research findings."
        mock_chat.send_message.return_value = mock_response
        
        mock_model_instance = MagicMock()
        mock_model_instance.start_chat.return_value = mock_chat
        mock_model.return_value = mock_model_instance

        agent = ResearchAgent(model_name="gemini-1.5-pro")
        result = agent.execute_task("Find something")
        
        self.assertEqual(result, "Research findings.")

if __name__ == '__main__':
    unittest.main()
