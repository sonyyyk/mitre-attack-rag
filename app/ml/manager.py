from app.ml.clusterer import TechniqueClusterer


class MLManager:
    """
    High-level interface for machine learning.
    """

    def __init__(self):

        self.clusterer = TechniqueClusterer()

    def cluster_embeddings(
        self,
        embeddings: list[list[float]]
    ) -> list[int]:

        return self.clusterer.fit_predict(
            embeddings
        )