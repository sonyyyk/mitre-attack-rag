from app.mitre.explorer import MITREExplorer
from app.mitre.models import AttackTechnique


class MITREParser:
    """
    Parse MITRE ATT&CK techniques.
    """

    def __init__(self):
        self.explorer = MITREExplorer()

    def get_attack_patterns(self) -> list:
        """
        Return all ATT&CK techniques.
        """

        objects = self.explorer.load_database()["objects"]

        attack_patterns = []

        for obj in objects:
            if obj.get("type") == "attack-pattern":
                attack_patterns.append(obj)

        return attack_patterns

    def get_mitre_id(self, technique: dict) -> str:
        """
        Extract MITRE ATT&CK ID.
        """

        references = technique.get("external_references", [])

        for reference in references:
            if reference.get("source_name") == "mitre-attack":
                return reference.get("external_id", "")

        return ""

    def get_tactics(self, technique: dict) -> list[str]:
        """
        Extract ATT&CK tactics.
        """

        phases = technique.get("kill_chain_phases", [])

        return [
            phase.get("phase_name")
            for phase in phases
        ]

    def parse_attack_pattern(self, technique: dict) -> AttackTechnique:
        """
        Convert one ATT&CK technique into our model.
        """

        return AttackTechnique(
            mitre_id=self.get_mitre_id(technique),
            name=technique.get("name", ""),
            description=technique.get("description", ""),
            platforms=technique.get("x_mitre_platforms", []),
            tactics=self.get_tactics(technique),
            is_subtechnique=technique.get(
                "x_mitre_is_subtechnique",
                False,
            ),
        )

    def parse_all_attack_patterns(self) -> list[AttackTechnique]:
        """
        Parse all ATT&CK techniques.
        """

        attack_patterns = self.get_attack_patterns()

        return [
            self.parse_attack_pattern(pattern)
            for pattern in attack_patterns
        ]