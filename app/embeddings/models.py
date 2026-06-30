from dataclasses import dataclass

from app.mitre.models import AttackTechnique


@dataclass
class EmbeddedTechnique:

    technique: AttackTechnique

    document: str

    embedding: list[float]