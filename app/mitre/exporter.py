import json
from pathlib import Path

from app.mitre.models import AttackTechnique


class MITREExporter:
    """
    Export parsed techniques.
    """

    OUTPUT_DIR = Path("data/processed")
    OUTPUT_FILE = OUTPUT_DIR / "techniques.json"

    def export(self, techniques: list[AttackTechnique]):

        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        data = [
            technique.__dict__
            for technique in techniques
        ]

        with open(
            self.OUTPUT_FILE,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"✅ Exported {len(data)} techniques")
        print(f"📁 {self.OUTPUT_FILE}")