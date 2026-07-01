from dataclasses import dataclass

from app.mitre.models import AttackTechnique


@dataclass
class EmbeddedTechnique:
    """
    MITRE technique with its embedding.
    """

    technique: AttackTechnique

    embedding: list[float]