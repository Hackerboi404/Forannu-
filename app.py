import os
import threading
import asyncio
from flask import Flask
from bot import start_bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Alive! 🤖"

def run_bot():
    asyncio.run(start_bot())

if __name__ == "__main__":
    print("🚀 Starting Server + Bot...")

    # Bot background me
    t = threading.Thread(target=run_bot)
    t.start()

    # Render port fix (VERY IMPORTANT)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
