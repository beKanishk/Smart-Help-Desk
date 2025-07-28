from agno.memory.v2.memory import Memory
from agno.memory.v2.db.mongodb import MongoMemoryDb

memory_db = MongoMemoryDb(
    collection_name="user_memories",
    db_url="mongodb://localhost:27017/helpdesk_db",  # or your cloud URI
    db_name="helpdesk_db"
)

memory = Memory(db=memory_db)



