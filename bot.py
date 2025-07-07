from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
import logging
from config import Config

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class autocaption(Client):
    
    async def on_message(self, message: Message):
        # Your message handling logic here
        pass

if __name__ == "__main__":
    app = autocaption(
        "Captioner",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=dict(
            root="plugins"
        )
    )
    app.run()


@app.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**👋 Welcome!**\n\n"
        "I'm a bot that auto locks/unlocks media in groups based on a timer.\n\n"
        "➕ Add me to your group and give admin rights.\n"
        "📍 Use /help to set it up.",
        quote=True
    )
