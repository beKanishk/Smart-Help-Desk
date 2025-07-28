from agno.agent import Agent
from agno.models.google import Gemini
from tools.order_tools import check_order, issue_refund, cancel_order, all_orders
from config import GOOGLE_API_KEY
from tools.user_tools import get_user
from Memory.MongoMemoryDb import memory


# This is the agent with MongoDB memory
# status_agent = Agent(
#     name="Change Status Agent",
#     role="Handles order status changes such as refunds and cancellations",
#     model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
#     tools=[check_order, issue_refund, cancel_order, get_user, all_orders],
#     instructions=[
#         "Before taking any decision check the order status using the check_order tool.",
#         "If the order is already refunded, inform the user.",
#         "If the order is delivered, then do not cancel it.",
#         "If the order is not delivered, proceed with cancellation.",
#         "If want to check user details use get_user tool",
#         "If want to check all orders of a user use all_orders tool",
#         "Give user details in well formatted way",
#         "Also save session_id in memory for future reference."
#     ],
#     markdown=True,
#     show_tool_calls=True,
#     memory=memory,
#     enable_user_memories=False,
#     enable_session_summaries=False,
#     add_history_to_messages=True,
#     num_history_runs=5,
# )



# This is the agent without MongoDB memory agno have in built-in memory if we pass session_id and user_id
status_agent = Agent(
    name="Change Status Agent",
    role="Handles order status changes such as refunds and cancellations",
    model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
    tools=[check_order, issue_refund, cancel_order, get_user, all_orders],
    instructions=[
        "First get the user details using the get_user tool.",
        "Before taking any decision check the order status using the check_order tool.",
        "If the order is already refunded, inform the user.",
        "If the order is delivered, then do not cancel it.",
        "If the order is not delivered, proceed with cancellation.",
        "If want to check user details use get_user tool",
        "If want to check all orders of a user use all_orders tool",
        "Give user details in well formatted way",
        "Also save session_id in memory for future reference."
    ],
    markdown=True,
    show_tool_calls=True,
)