import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

file = os.getenv("DATABASE") or "messages.db"
test_file = os.getenv("TESTDATABASE") or "test_messages.db"
DATABASE = os.path.join(dirname, "..", "data", file)
TESTDATABASE = os.path.join(dirname, "..", "data", test_file)
