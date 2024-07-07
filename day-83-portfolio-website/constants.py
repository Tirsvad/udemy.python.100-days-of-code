import os

# Locale path
BASE_PATH = f"{os.path.dirname(os.path.realpath(__file__))}{os.path.sep}"
INSTANCE = f"{BASE_PATH}instance{os.path.sep}"

DB_FILE = f"{INSTANCE}portfolio.db"
