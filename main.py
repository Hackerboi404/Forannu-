import os
import threading
from flask import Flask
from bot import start_bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Alive! 🤖"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    print("🚀 Starting Server + Bot...")

    # Bot ko background thread mein start karo
    # start_bot function ab apna loop khud handle karega
    t = threading.Thread(target=start_bot, daemon=True)
    t.start()

    # Flask ko main thread mein rakho
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
