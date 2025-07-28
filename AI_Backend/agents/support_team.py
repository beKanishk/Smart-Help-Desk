from agno.team.team import Team
from agno.models.google import Gemini
from .status_agent import status_agent
from .knowledge_agent import knowledge_agent
from config import GOOGLE_API_KEY
from MongoMemoryDb import memory

# support_team = Team(
#     members=[status_agent, knowledge_agent],
#     model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
#     mode="coordinate",
#     success_criteria="Select the best agent to handle the query",
#     instructions=[
#         "For order/refund/cancel questions, use Status Agent.",
#         "For general queries, use Knowledge Agent."
#     ],
#     markdown=True,
#     show_tool_calls=True,
# )

support_team = Team(
    members=[status_agent, knowledge_agent],
    model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
    memory=memory,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_messages=True,
    num_history_runs=5,
    mode="coordinate",
    success_criteria="Select the best agent to handle the query",
    instructions=[
        "For order/refund/cancel questions, use Status Agent.",
        "For general queries, use Knowledge Agent.",
        "Also save session_id in memory for future reference.",
    ],
    markdown=True,
    show_tool_calls=True,
)
