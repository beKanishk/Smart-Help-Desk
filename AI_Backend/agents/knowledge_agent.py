from agno.agent import Agent
from agno.models.google import Gemini
from config import GOOGLE_API_KEY
knowledge_agent = Agent(
    name="Knowledge Agent",
    role="Answers FAQs and general helpdesk questions",
    model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
    markdown=True,
    show_tool_calls=True,
)
