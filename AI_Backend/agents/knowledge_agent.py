# # from agno.agent import Agent
# # from agno.models.google import Gemini
# # from agno.vectordb.chroma import ChromaDb
# # from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
# # from config import GOOGLE_API_KEY, genai

# # # 1. Initialize ChromaDB
# # vector_db = ChromaDb(
# #     collection="company_policies",
# #     path="chroma_db",         # Persistent storage path
# #     persistent_client=True,
# #     embedding_function=lambda text: genai.embed_content(
# #         model="models/text-embedding-004", 
# #         content=text
# #     )['embedding'],
# # )

# # # 2. Create Knowledge Base (PDF embeddings)
# # knowledge_base = PDFKnowledgeBase(
# #     path="C:/Users/akani/Downloads/Smiley.pdf",  # Your PDF(s)
# #     vector_db=vector_db,
# #     chunk_size=500,
# #     reader=PDFReader(chunk=True), # Use pypdf to read PDF
# # )

# # # Load embeddings into ChromaDB (only once)
# # # Set recreate=True to refresh embeddings
# # knowledge_base.load(recreate=False)

# # # 3. Knowledge Agent
# # knowledge_agent = Agent(
# #     name="Knowledge Agent",
# #     role="Answers FAQs and company policy-related questions",
# #     model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
# #     knowledge=knowledge_base,          # Attach ChromaDB-backed knowledge
# #     search_knowledge=True,             # Enable vector search
# #     instructions=[
# #         "You are a helpful assistant that answers questions based on company policies.",
# #         "Always use the knowledge base context to answer questions accurately.",
# #         "If the question is not related to company policies, politely inform the user.",
# #     ],
# #     markdown=True,
# #     show_tool_calls=True,
# # )


# from agno.agent import Agent
# from agno.models.google import Gemini
# from agno.vectordb.chroma import ChromaDb
# from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
# from agno.embedder.base import Embedder
# from config import GOOGLE_API_KEY, genai

# # Create a custom embedder for Google's embedding model
# class GoogleEmbedder(Embedder):
#     def __init__(self):
#         super().__init__()
#         self.dimensions = 768  # Gemini embeddings dimension (check docs)

#     def get_embedding_and_usage(self, text: str):
#         """Return embedding and usage info (usage can be empty)."""
#         response = genai.embed_content(
#             model="models/text-embedding-004",
#             content=text
#         )
#         embedding = response['embedding']
#         return embedding, {}  # Empty dict for usag

# # 1. Initialize ChromaDB with the custom embedder
# vector_db = ChromaDb(
#     collection="company_policies",
#     path="chroma_db",
#     persistent_client=True,
#     embedder=GoogleEmbedder()  # Use the custom embedder here
# )

# # 2. Create Knowledge Base (PDF embeddings)
# knowledge_base = PDFKnowledgeBase(
#     path="C:/Users/akani/Downloads/Smiley.pdf",
#     vector_db=vector_db,
#     chunk_size=500,
#     reader=PDFReader(chunk=True),
#     # Remove embedding_function - it's handled by the embedder in vector_db
# )
# docs = vector_db.search("leave policy", top_k=2)
# print("Search Results:", docs)
# # Load embeddings into ChromaDB (only once)
# knowledge_base.load(recreate=True)

# # 3. Knowledge Agent
# knowledge_agent = Agent(
#     name="Knowledge Agent",
#     role="Answers FAQs and company policy-related questions",
#     model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
#     knowledge=knowledge_base,
#     search_knowledge=True,
#     instructions=[
#         "You are a helpful assistant that answers questions based on company policies.",
#         "Always use the knowledge base context to answer questions accurately.",
#         "If the question is not related to company policies, politely inform the user.",
#     ],
#     markdown=True,
#     show_tool_calls=True,
# )

from agno.agent import Agent
from agno.models.google import Gemini
from agno.vectordb.chroma import ChromaDb
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.embedder.google import GeminiEmbedder
from config import GOOGLE_API_KEY
import os

# 1. Ensure Google API Key set
if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY not set")

# 2. Initialize ChromaDB with GeminiEmbedder
vector_db = ChromaDb(
    collection="company_policies",
    path="chroma_db",
    persistent_client=True,
    embedder=GeminiEmbedder(
        api_key=GOOGLE_API_KEY,
        dimensions=768
    )
)

# 3. Prepare PDF knowledge base
PDF_PATH = r"C:\Users\akani\Downloads\Smiley.pdf"
if not os.path.exists(PDF_PATH):
    raise FileNotFoundError(f"Policy PDF not found: {PDF_PATH}")

knowledge_base = PDFKnowledgeBase(
    path=PDF_PATH,
    vector_db=vector_db,
    chunk_size=500
)

# Load chunks into ChromaDB (only once)
knowledge_base.load(recreate=False)

# 4. Configure Knowledge Agent with vector retrieval support
knowledge_agent = Agent(
    name="Knowledge Agent",
    role="Answers questions based on company policy PDF.",
    model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
    knowledge=knowledge_base,
    search_knowledge=True,
    instructions=[
        "You are a helpful assistant that answers questions from the company policy.",
        "Use context from the provided knowledge base to answer accurately.",
        "If insufficient information exists, inform the user politely."
    ],
    markdown=True,
    show_tool_calls=True,
)
