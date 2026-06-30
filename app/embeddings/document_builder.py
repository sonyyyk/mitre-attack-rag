from app.mitre.models import AttackTechnique


class DocumentBuilder:
    """
    Build a text document from a MITRE ATT&CK technique.
    """

    def build(self, technique: AttackTechnique) -> str:

        document = f"""
MITRE Technique: {technique.mitre_id}

Name:
{technique.name}

Description:
{technique.description}

Platforms:
{", ".join(technique.platforms)}

Tactics:
{", ".join(technique.tactics)}
"""

        return document.strip()