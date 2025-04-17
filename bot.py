import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Pattern to match mobile.de URLs and extract the ID
MOBILE_DE_REGEX = r"https://m\.mobile\.de/auto-inserat/[^/]+/(\d+)\.html"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        return

    matches = re.findall(MOBILE_DE_REGEX, update.message.text)
    for match in matches:
        new_url = f"https://suchen.mobile.de/fahrzeuge/details.html?id={match}"
        await update.message.reply_text(new_url)

if __name__ == '__main__':
    import os

    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8121269919:AAHjF5tcuanD1W1YIP_v_3-wvZjRY9aQCMI")  # Or just paste your token as a string here
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot is running...")
    app.run_polling()