from fastapi import FastAPI
from pydantic import BaseModel
from agents.support_team import support_team
from agno.agent import RunResponse

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/agent/respond")
async def respond(query: Query):
    result : RunResponse = await support_team.arun(query.query)
    return {"response": result.content}
