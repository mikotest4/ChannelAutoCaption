import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7819249411:AAESmQV0hlmNqyakQEAXfZzt-Jiu4WTgLTw")
    API_ID = int(os.environ.get("API_ID", "27704224"))
    API_HASH = os.environ.get("API_HASH", "c2e33826d757fe113bc154fcfabc987d")
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Koi:aloksingh@cluster0.86wo9.mongodb.net/?retryWrites=true&w=majority")
