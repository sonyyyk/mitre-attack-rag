from sentence_transformers import SentenceTransformer

from app.embeddings.config import MODEL_NAME


class EmbeddingEncoder:
    """
    Encode text into vector embeddings.
    """

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(MODEL_NAME)

        print("Embedding model loaded.")

    def encode(self, document: str) -> list[float]:
        """
        Encode a document into an embedding vector.
        """

        embedding = self.model.encode(
            document,
            convert_to_numpy=True
        )

        return embedding.tolist()