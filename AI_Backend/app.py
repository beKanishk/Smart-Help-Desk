from fastapi import FastAPI
from pydantic import BaseModel
from agents.support_team import support_team
from agno.agent import RunResponse

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/agent/respond")
def respond(query: Query):
    result : RunResponse = support_team.run(query.query)
    return {"response": result.content}
