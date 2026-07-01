from sklearn.cluster import KMeans


class TechniqueClusterer:
    """
    Cluster MITRE ATT&CK embeddings.
    """

    def __init__(self):

        self.model = KMeans(
            n_clusters=10,
            random_state=42,
            n_init="auto"
        )

    def fit_predict(
        self,
        embeddings: list[list[float]]
    ) -> list[int]:
        """
        Cluster embeddings.
        """

        return self.model.fit_predict(embeddings).tolist()