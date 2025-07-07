import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7845096754:AAGp_ydOCzsjrC89b3LOWHzuWG4gKTdK2uI")
    API_ID = int(os.environ.get("API_ID", 29245477))
    API_HASH = os.environ.get("API_HASH", "0abc83883262245c90ca337b7a0375c4")
    DB_URL = os.environ.get("DATABASE_URL", "postgresql+asyncpg://neondb_owner:npg_XbwV4SzKFn7G@ep-steep-feather-a8wgninx-pooler.eastus2.azure.neon.tech/neondb")
