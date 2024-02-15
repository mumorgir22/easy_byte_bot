import logging

import requests

from config.settings import API_KEY


# Функция для получения данных о курсах валют и записи их в currency_data
def fetch_and_store_data() -> dict | None:
    url: str = f"https://api.currencyapi.com/v3/latest?apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        currency_data = response.json()["data"]
        return currency_data
    else:
        logging.error("Ошибка при получении данных о курсах валют")
        return None
