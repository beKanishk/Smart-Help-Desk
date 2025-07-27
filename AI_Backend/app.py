from fastapi import FastAPI, Header
from pydantic import BaseModel
from agents.support_team import support_team
from auth_state import jwt_state
from agno.agent import RunResponse

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/agent/respond")
async def respond(query: Query, authorization: str = Header(...)):
    jwt_state["jwt"] = authorization
    result: RunResponse = await support_team.arun(query.query)
    return {"response": result.content}

