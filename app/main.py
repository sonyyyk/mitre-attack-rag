from app.mitre.exporter import MITREExporter
from app.mitre.parser import MITREParser


def main():

    parser = MITREParser()

    exporter = MITREExporter()

    techniques = parser.parse_all_attack_patterns()

    print(f"Loaded techniques: {len(techniques)}")

    exporter.export(techniques)


if __name__ == "__main__":
    main()