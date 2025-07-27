from agno.agent import Agent
from agno.models.google import Gemini
from tools.order_tools import check_order, issue_refund, cancel_order, all_orders
from config import GOOGLE_API_KEY
from tools.user_tools import get_user

status_agent = Agent(
    name="Change Status Agent",
    role="Handles order status changes such as refunds and cancellations",
    model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
    tools=[check_order, issue_refund, cancel_order, get_user, all_orders],
    instructions=[
        "Before taking any decision check the order status using the check_order tool.",
        "If the order is already refunded, inform the user.",
        "If the order is delivered, then do not cancel it.",
        "If the order is not delivered, proceed with cancellation.",
        "If want to check user details use get_user tool",
        "If want to check all orders of a user use all_orders tool",
        "Give user details in well formatted way"
    ],
    markdown=True,
    show_tool_calls=True,
)
