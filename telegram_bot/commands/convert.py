from telegram import Update
from telegram.ext import CallbackContext


async def convert_command(
    update: Update, context: CallbackContext, currency_data: dict | None
) -> None:
    if currency_data:
        try:
            args: list = context.args
            amount: float = float(args[0])
            from_currency: str = args[1].upper()
            to_currency: str = args[3].upper()

            if from_currency not in currency_data or to_currency not in currency_data:
                await update.message.reply_text(
                    "Одна из введенных валют не найдена. Пожалуйста, проверьте правильность ввода."
                )
            else:
                currency: float = currency_data[from_currency]["value"]
                new_currency: float = currency_data[to_currency]["value"]
                result: float = amount * new_currency / currency
                await update.message.reply_text(
                    f"{amount} {from_currency} = {round(result, 2)} {to_currency}"
                )

        except (IndexError, ValueError):
            await update.message.reply_text(
                "Используйте команду в формате /convert <сумма> <из валюты> <в валюту>. Например: /convert 100 USD to EUR."
            )
    else:
        await update.message.reply_text(
            "Данные о курсах валют еще не загружены. Пожалуйста, подождите."
        )
