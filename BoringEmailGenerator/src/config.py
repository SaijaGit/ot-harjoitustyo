import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

# jos os.getenv("FOO") palauttaa arvon None, FOO saa arvokseen "default bar"
DATABASE = os.getenv("DATABASE") or "messages.db"
TESTDATABASE = os.getenv("TESTDATABASE") or "test_messages.db"