import logging

from httpx import Client

from app.mitre.config import MITRE_DIR, MITRE_FILE, MITRE_URL


logger = logging.getLogger(__name__)


class MITREDownloader:
    """
    Downloads the official MITRE ATT&CK database.
    """

    def download_database(self) -> None:
        """
        Download the latest MITRE ATT&CK STIX database.
        """

        logger.info("Downloading MITRE ATT&CK database...")

        MITRE_DIR.mkdir(parents=True, exist_ok=True)

        with Client(timeout=60) as client:

            response = client.get(MITRE_URL)

            response.raise_for_status()

            MITRE_FILE.write_bytes(response.content)

        logger.info("MITRE ATT&CK database downloaded successfully.")