from agno.team.team import Team
from agno.models.google import Gemini
from .refund_agent import refund_agent
from .knowledge_agent import knowledge_agent
from config import GOOGLE_API_KEY

support_team = Team(
    members=[refund_agent, knowledge_agent],
    model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
    mode="coordinate",
    success_criteria="Select the best agent to handle the query",
    instructions=[
        "For order/refund questions, use Refund Agent.",
        "For general queries, use Knowledge Agent."
    ],
    markdown=True,
    show_tool_calls=True,
)
