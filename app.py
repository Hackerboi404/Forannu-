import os
import threading
from flask import Flask
from bot import start_bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Alive! 🤖"

if __name__ == "__main__":
    print("🚀 Starting Server + Bot...")

    # 🔥 NO asyncio loop here
    t = threading.Thread(target=start_bot)
    t.start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
