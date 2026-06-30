from dataclasses import dataclass


@dataclass
class AttackTechnique:
    """
    Simplified MITRE ATT&CK technique.
    """

    mitre_id: str
    name: str
    description: str
    platforms: list[str]
    tactics: list[str]
    is_subtechnique: bool