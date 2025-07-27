import chromadb
from chromadb.utils import embedding_functions
from pypdf import PdfReader
from config import genai

# Initialize Chroma
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("company_policies")

# Read PDF
reader = PdfReader("C:/Users/akani/Downloads/Smiley.pdf")
all_text = ""
for page in reader.pages:
    all_text += page.extract_text()

# Split into chunks
def chunk_text(text, chunk_size=500):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size
    return chunks


chunks = chunk_text(all_text)

# Gemini embedding function
def embed_text(text):
    response = genai.embed_content(model="models/text-embedding-004", content=text)
    return response['embedding']

# Store in Chroma
for idx, chunk in enumerate(chunks):
    embedding = embed_text(chunk)
    collection.add(ids=[str(idx)], documents=[chunk], embeddings=[embedding])

print("Company policy embeddings stored in ChromaDB.")
