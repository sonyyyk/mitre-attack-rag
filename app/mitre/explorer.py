import json
from collections import Counter

from app.mitre.config import MITRE_FILE

class MITREExplorer:
    """
    Explore and analyze the MITRE ATT&CK STIX database.
    """

    def load_database(self) -> dict:
        """
        Load the MITRE ATT&CK database from the local JSON file.
        """

        with open(MITRE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    def count_objects(self) -> int:
        """
        Count the total number of objects in the MITRE ATT&CK database.
        """

        database = self.load_database()

        return len(database["objects"])
    
    def count_object_types(self) -> Counter:
        """
         Count all MITRE ATT&CK object types.
        """

        objects = self.load_database()["objects"]

        object_types = [obj["type"] for obj in objects]

        return Counter(object_types)