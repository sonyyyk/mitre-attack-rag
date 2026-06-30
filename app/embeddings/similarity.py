from sentence_transformers.util import cos_sim


class SimilarityEngine:
    """
    Compare two embeddings.
    """

    def compare(
        self,
        embedding1: list[float],
        embedding2: list[float]
    ) -> float:

        similarity = cos_sim(
            embedding1,
            embedding2
        )

        return float(similarity.item())