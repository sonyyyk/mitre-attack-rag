from app.mitre.explorer import MITREExplorer


class MITREParser:
    """
    Parse MITRE ATT&CK objects.
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

            if obj["type"] == "attack-pattern":

                attack_patterns.append(obj)

        return attack_patterns    