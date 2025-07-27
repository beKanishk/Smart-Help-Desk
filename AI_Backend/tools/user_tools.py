import httpx
from agno.tools import tool
from auth_state import jwt_state

SPRING_BOOT_BASE_URL = "http://localhost:8080/api/users"

def get_headers():
    jwt = jwt_state.get("jwt")
    if not jwt:
        raise Exception("JWT token not set")

    # If jwt is a dict, extract the Authorization key
    if isinstance(jwt, dict):
        jwt = jwt.get("Authorization", "")

    if not jwt.startswith("Bearer "):
        jwt = f"Bearer {jwt}"

    return {"Authorization": jwt}

@tool
async def get_user() :
    """Get the User details"""
    async with httpx.AsyncClient(headers=get_headers()) as client:
        resp = await client.get(f"{SPRING_BOOT_BASE_URL}")
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"Failed to get user. Response: {resp.text}"}