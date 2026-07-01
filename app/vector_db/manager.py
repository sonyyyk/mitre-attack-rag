from app.vector_db.client import VectorClient
from app.vector_db.config import COLLECTION_NAME


class VectorDBManager:
    """
    Manage ChromaDB vector database.
    """

    def __init__(self):

        client = VectorClient()

        self.collection = client.get_client().get_or_create_collection(
            name=COLLECTION_NAME
        )

    def clear(self):
        """
        Remove all vectors from collection.
        """

        ids = self.collection.get()["ids"]

        if ids:
            self.collection.delete(ids=ids)

    def add_documents(
        self,
        techniques,
        embeddings,
    ):
        """
        Store MITRE techniques in ChromaDB.
        """

        ids = []
        documents = []
        metadatas = []

        for technique, embedding in zip(
            techniques,
            embeddings,
        ):

            ids.append(
                technique.mitre_id
            )

            document = (
                f"{technique.name}\n\n"
                f"{technique.description}"
            )

            documents.append(
                document
            )

            metadatas.append(
                {
                    "mitre_id": technique.mitre_id,
                    "name": technique.name,
                    "tactics": ", ".join(
                        technique.tactics
                    ),
                    "platforms": ", ".join(
                        technique.platforms
                    ),
                }
            )

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

    def search_text(
        self,
        text: str,
        encoder,
        top_k: int = 5,
    ):
        """
        Search techniques using text.
        """

        embedding = encoder.encode(text)

        return self.search(
            embedding,
            top_k,
        )

    def count(self):
        """
        Return number of stored vectors.
        """

        return self.collection.count()