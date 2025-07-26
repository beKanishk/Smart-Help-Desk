from agno.agent import Agent
from agno.models.google import Gemini
from tools.order_tools import check_order, issue_refund
from config import GOOGLE_API_KEY

refund_agent = Agent(
    name="Refund Agent",
    role="Handles order tracking and refund requests",
    model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
    tools=[check_order, issue_refund],
    instructions=[
        "Before refunding check the order status.",
        "If the order is already refunded, inform the user.",
    ],
    markdown=True,
    show_tool_calls=True,
)
