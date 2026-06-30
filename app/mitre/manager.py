from app.mitre.config import MITRE_FILE
from app.mitre.downloader import MITREDownloader


class MITREKnowledgeBase:
    """
    Main interface for working with the MITRE ATT&CK knowledge base.
    """

    def initialize(self) -> None:
        """
        Prepare the local MITRE knowledge base.
        """

        if MITRE_FILE.exists():
            print("✅ MITRE ATT&CK database found.")
        else:
            print("⚠️ MITRE ATT&CK database not found.")

            downloader = MITREDownloader()
            downloader.download_database()

            print("✅ MITRE ATT&CK database is ready.")