import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)

from telegram_bot.commands.convert import convert_command
from telegram_bot.commands.echo import echo_command
from telegram_bot.commands.help import help_command
from telegram_bot.commands.start import start_command
from telegram_bot.utils.api import fetch_and_store_data
from config.settings import TOKEN

currency_data = None
logging.basicConfig(
    filename="telegram_bot/bot.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def run_periodic_task(context) -> None:
    global currency_data
    currency_data = fetch_and_store_data()


async def convert(update: Update, context: CallbackContext) -> None:
    await convert_command(update, context, currency_data)


if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()
    job_queue = application.job_queue

    # Задача при запуске бота
    job_queue.run_once(run_periodic_task, when=0)
    # Задача для обновления данных по валюте, каждые 10 мин
    job_queue.run_repeating(run_periodic_task, interval=10 * 60)

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("convert", convert))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo_command)
    )

    application.run_polling(allowed_updates=Update.ALL_TYPES)
