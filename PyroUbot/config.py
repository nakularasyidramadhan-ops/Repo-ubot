import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "8709277364").split()))

API_ID = int(os.getenv("API_ID", "36303190"))

API_HASH = os.getenv("API_HASH", "79029cd65be6ae2a8f6a5668d94485c2")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8431183153:AAFla9mSBU2HepyRfVvOlEuggNmh11Q7puI")

OWNER_ID = int(os.getenv("OWNER_ID", "7233292382"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ibnumuzakim7:ibnumuzakim132@ibnumuzakim.sbwnig8.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4912568273"))
