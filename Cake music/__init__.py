from pyrogram import Client 
from config import *


app = Client(
    name="Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)
