from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import TOKEN, WEB_APP_URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏏 Neon Cricket\n\n"
        "Welcome to Neon Cricket!\n\n"
        "Rules:\n"
        "• Enter your name\n"
        "• Click Save\n"
        "• Start playing\n"
        "• Survive 30 balls\n"
        "• Score appears on leaderboard\n\n"
        "Good luck! 🚀"
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎮 Play", web_app=WebAppInfo(url=WEB_APP_URL))]]
    await update.message.reply_text(
        "🏏 Neon Cricket Game\n\nClick below to play 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# 🔥 IMPORTANT: this is now a NORMAL function
def start_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))

    print("🤖 Bot Started...")

    # ❗ No await, no asyncio here
    app.run_polling(stop_signals=None)
