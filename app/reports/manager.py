from app.reports.recommendations import RecommendationManager
from app.reports.risk import RiskManager


class ReportManager:
    """
    Generate structured cyber threat report.
    """

    def __init__(self):

        self.risk = RiskManager()

        self.recommendations = RecommendationManager()

    def generate(
        self,
        query: str,
        results: dict,
    ) -> dict:

        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        techniques = []

        tactics = []

        platforms = []

        for metadata, distance in zip(
            metadatas,
            distances,
        ):

            tactic = metadata["tactics"]
            platform = metadata["platforms"]

            tactics.extend(
                tactic.split(", ")
            )

            platforms.extend(
                platform.split(", ")
            )

            similarity = round(
                (1 - distance) * 100,
                1
            )

            techniques.append(
                {
                    "id": metadata.get(
                        "mitre_id",
                        "Unknown"
                    ),

                    "name": metadata["name"],

                    "tactic": tactic,

                    "platform": platform,

                    "similarity": similarity,
                }
            )

        risk = self.risk.calculate(
            tactics
        )

        recommendations = self.recommendations.get(
            tactics
        )

        summary = (
            f"The analyzed incident is most closely related to "
            f"{len(techniques)} MITRE ATT&CK techniques. "
            f"The detected behavior indicates possible "
            f"{', '.join(sorted(set(tactics)))} activity."
        )

        return {

            "risk": risk,

            "summary": summary,

            "techniques": techniques,

            "recommendations": recommendations,

            "technique_count": len(
                techniques
            ),

            "platform_count": len(
                set(platforms)
            ),

            "tactic_count": len(
                set(tactics)
            ),
        }