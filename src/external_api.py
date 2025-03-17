import os

import requests
from dotenv import load_dotenv


def get_amount_of_transaction(transaction) -> float | None:
    try:
        amount = transaction.get("operationAmount").get("amount")
        currency = transaction.get("operationAmount").get("currency").get("code")
    except AttributeError:
        print('Ошибка в данных')
        return None
    if currency == 'RUB':
        return amount
    else:
        load_dotenv()
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={amount}"
        headers = {
            "apikey": os.getenv("API_KEY")
        }
        payload = {}
        try:
            response = requests.request("GET", url, headers=headers, data = payload)
            return response.json()['result']
        except requests.exceptions.RequestException as e:
            print(e)
            return None