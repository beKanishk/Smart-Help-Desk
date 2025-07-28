from fastapi import FastAPI, Header
from pydantic import BaseModel
from agents.support_team import support_team
from auth_state import jwt_state
from agno.agent import RunResponse
from tools.user_tools import get_user_data
from uuid import uuid4

app = FastAPI()

# Request body model for the agent query
class Query(BaseModel):
    query: str
    session_id: str | None = None

@app.post("/agent/respond")
async def respond(query: Query, authorization: str = Header(...)):
    jwt_state["jwt"] = authorization
    user = await get_user_data()
    user_id = user.get("id")
    session_id = query.session_id or str(uuid4())

    result: RunResponse = await support_team.arun(query.query, user_id=user_id, session_id=session_id)
    
    return {"response": result.content, "session_id": session_id, "user_id": user_id,}

