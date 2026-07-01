from app.vector_db.client import VectorClient
from app.vector_db.config import COLLECTION_NAME


class VectorDBManager:
    """
    Manage vector database.
    """

    def __init__(self):

        client = VectorClient()

        self.collection = client.get_client().get_or_create_collection(
            name=COLLECTION_NAME
        )

    def add_documents(
        self,
        ids,
        documents,
        embeddings,
        metadatas,
    ):
        """
        Add documents to ChromaDB.
        """

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def search(
        self,
        embedding,
        top_k=5,
    ):
        """
        Search similar techniques.
        """

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

    def count(self):

        return self.collection.count()
    def search_text(
        self,
        text: str,
        encoder,
        top_k: int = 5,
        ):
        """
        Search techniques using text query.
        """

        embedding = encoder.encode(text)

        return self.search(
            embedding,
            top_k,
        )