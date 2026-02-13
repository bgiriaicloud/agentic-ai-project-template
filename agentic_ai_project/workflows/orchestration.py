import asyncio
import os
from dotenv import load_dotenv
from agentic_ai_project.agents.research_agent import ResearchAgent
from agentic_ai_project.agents.code_agent import CodeAgent
from agentic_ai_project.observability.logging import setup_logging
from agentic_ai_project.guardrails.safety_checks import SafetyGuardrails

# Load environment variables
load_dotenv()


def run_agentic_team(task: str):
    setup_logging()
    
    # Check for API Key
    if not os.getenv("GOOGLE_API_KEY"):
        return {"error": "GOOGLE_API_KEY not found in environment variables."}

    print(f"\n[Orchestrator] Processing task: {task}")
    
    if not SafetyGuardrails.check_input(task):
        return {"error": "Task rejected by safety guardrails."}

    model_name = "gemini-1.5-pro-latest"
    researcher = ResearchAgent(model_name=model_name)
    coder = CodeAgent(model_name=model_name)

    print(f"\n[Orchestrator] Assigning task to Researcher...")
    research_result = researcher.execute_task(task)
    
    print(f"\n[Orchestrator] Assigning task to Coder...")
    code_task = f"Based on these findings: {research_result}\nWrite a python script to implement the solution for: {task}"
    code_result = coder.execute_task(code_task)
    
    if not SafetyGuardrails.check_output(code_result):
         return {"error": "Code output rejected by safety guardrails."}

    return {
        "research_findings": research_result,
        "generated_code": code_result
    }

def main():
    task = input("Enter a task for the agentic team: ")
    result = run_agentic_team(task)
    
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"\n[Researcher] Findings:\n{result['research_findings']}")
        print(f"\n[Coder] Solution:\n{result['generated_code']}")

if __name__ == "__main__":
    main()


