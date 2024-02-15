from telegram import Update
from telegram.ext import CallbackContext


async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start - начать использование бота\n"
        "/help - получить справку о доступных командах\n"
        "/convert <сумма> <из валюты> to <в валюту> - конвертировать валюту"
    )
