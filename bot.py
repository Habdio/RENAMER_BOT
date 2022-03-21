from pyrogram import Client
import os

TOKEN = ("5231358216:AAF1OnZm9Ay9xHhizQZrV6jleLNjNFbyck4")

APP_ID = ("10342078")

API_HASH = ("09ca4ef17b06c5030d4e8f7cbd92f1a9")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
