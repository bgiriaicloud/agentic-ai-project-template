from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agentic_ai_project.workflows.orchestration import run_agentic_team
import os

app = FastAPI(title="Agentic AI API", version="1.0.0")

class TaskRequest(BaseModel):
    query: str

class TaskResponse(BaseModel):
    research_findings: str
    generated_code: str

@app.get("/")
def read_root():
    return {"status": "Agentic AI Service is running"}

@app.post("/agent/run", response_model=TaskResponse)
def run_agent(request: TaskRequest):
    if not os.getenv("GOOGLE_API_KEY"):
        raise HTTPException(status_code=500, detail="Server misconfiguration: API Key missing")
        
    result = run_agentic_team(request.query)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
        
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
