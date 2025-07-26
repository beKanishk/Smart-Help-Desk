import httpx
from agno.tools import tool

SPRING_BOOT_BASE_URL = "http://localhost:8080/api/orders"

@tool
async def check_order(order_id: str) -> str:
    """Check the status of an order by its ID."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{SPRING_BOOT_BASE_URL}/{order_id}")
        if resp.status_code == 200:
            return f"Order details: {resp.json()}"
        return f"Failed to retrieve order {order_id}. Response: {resp.text}"

@tool
async def issue_refund(order_id: str) -> str:
    """Issue a refund for an order."""
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{SPRING_BOOT_BASE_URL}/{order_id}/refund")
        if resp.status_code == 200:
            return f"Refund processed: {resp.json()}"
        return f"Refund failed for order {order_id}. Response: {resp.text}"

@tool
async def cancel_order(order_id: str) -> str:
    """Cancel an order by its ID."""
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{SPRING_BOOT_BASE_URL}/{order_id}/cancel")
        if resp.status_code == 200:
            return f"Order canceled: {resp.json()}"
        return f"Failed to cancel order {order_id}. Response: {resp.text}"
