import google.generativeai as genai
from typing import Dict, Any

class ToolDefinitions:
    @staticmethod
    def get_search_tool():
        # Example defining a tool for Gemini
        search_tool = genai.protos.Tool(
            function_declarations=[
                genai.protos.FunctionDeclaration(
                    name="search_web",
                    description="Searching the web for current information.",
                    parameters=genai.protos.Schema(
                        type=genai.protos.Type.OBJECT,
                        properties={
                            "query": genai.protos.Schema(
                                type=genai.protos.Type.STRING,
                                description="The search query"
                            )
                        },
                        required=["query"]
                    )
                )
            ]
        )
        return search_tool

    @staticmethod
    def get_calculator_tool():
        calculator_tool = genai.protos.Tool(
             function_declarations=[
                genai.protos.FunctionDeclaration(
                    name="calculate",
                    description="Perform mathematical calculations.",
                    parameters=genai.protos.Schema(
                        type=genai.protos.Type.OBJECT,
                        properties={
                            "expression": genai.protos.Schema(
                                type=genai.protos.Type.STRING,
                                description="The mathematical expression to evaluate"
                            )
                        },
                        required=["expression"]
                    )
                )
            ]
        )
        return calculator_tool
