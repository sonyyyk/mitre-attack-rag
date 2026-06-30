from app.embeddings.config import EMBEDDINGS_FILE
from app.embeddings.document_builder import DocumentBuilder
from app.embeddings.encoder import EmbeddingEncoder
from app.embeddings.storage import EmbeddingStorage
from app.mitre.models import AttackTechnique


class EmbeddingManager:
    """
    High-level interface for embedding generation.
    """

    def __init__(self):

        self.builder = DocumentBuilder()

        self.encoder = EmbeddingEncoder()

        self.storage = EmbeddingStorage(
            EMBEDDINGS_FILE
        )

    def create_embedding(
        self,
        technique: AttackTechnique
    ) -> list[float]:
        """
        Create embedding for a single technique.
        """

        document = self.builder.build(technique)

        return self.encoder.encode(document)

    def create_embeddings(
        self,
        techniques: list[AttackTechnique]
    ) -> list[list[float]]:
        """
        Create embeddings for all techniques.
        """

        embeddings = []

        total = len(techniques)

        for index, technique in enumerate(techniques, start=1):

            print(f"[{index}/{total}] Encoding: {technique.name}")

            embedding = self.create_embedding(technique)

            embeddings.append(embedding)

        return embeddings

    def save_embeddings(
        self,
        embeddings: list[list[float]]
    ) -> None:
        """
        Save embeddings to disk.
        """

        self.storage.save(embeddings)

    def load_embeddings(
        self
    ) -> list[list[float]]:
        """
        Load embeddings from disk.
        """

        return self.storage.load()

    def embeddings_exist(
        self
    ) -> bool:
        """
        Check if embeddings already exist.
        """

        return self.storage.exists()