import chromadb

from app.vector_db.config import CHROMA_PATH


class VectorClient:
    """
    Create ChromaDB client.
    """

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_PATH)
        )

    def get_client(self):

        return self.client