from telegram import Update
from telegram.ext import CallbackContext

from telegram_bot.commands.help import help_command


async def echo_command(update: Update, context: CallbackContext) -> None:
    user_text: str = update.message.text.lower()
    if any(
        word in user_text for word in ["привет", "hello", "здравствуй", "здравствуйте"]
    ):
        await update.message.reply_text(
            "Привет! Я готов помочь вам с конвертацией валют. Для получения списка команд используй /help."
        )
    elif any(word in user_text for word in ["пока", "до свидания", "спасибо"]):
        await update.message.reply_text(
            "До свидания! Если вам понадобится еще помощь, обращайтесь."
        )
    else:
        await help_command(update, context)
