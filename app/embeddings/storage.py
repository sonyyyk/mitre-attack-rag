import pickle
from pathlib import Path


class EmbeddingStorage:
    """
    Save and load embeddings.
    """

    def __init__(self, path: Path):

        self.path = path

    def save(self, embeddings: list[list[float]]) -> None:
        """
        Save embeddings to disk.
        """

        self.path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.path, "wb") as file:
            pickle.dump(embeddings, file)

    def load(self) -> list[list[float]]:
        """
        Load embeddings from disk.
        """

        with open(self.path, "rb") as file:
            return pickle.load(file)

    def exists(self) -> bool:

        return self.path.exists()