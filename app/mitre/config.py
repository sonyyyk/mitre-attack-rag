from pathlib import Path

# Коренева директорія проєкту
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Директорія для даних
DATA_DIR = PROJECT_ROOT / "data"

# Директорія MITRE
MITRE_DIR = DATA_DIR / "mitre"

# Локальний файл MITRE
MITRE_FILE = MITRE_DIR / "enterprise-attack.json"

# Офіційне джерело MITRE ATT&CK
MITRE_URL = (
    "https://raw.githubusercontent.com/mitre/cti/master/"
    "enterprise-attack/enterprise-attack.json"
)