import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv


def get_amount_of_transaction(transaction: Dict[str, Any]) -> float | None:
    try:
        operation_amount = transaction.get("operationAmount", {})
        amount = float(operation_amount.get("amount"))
        currency = operation_amount.get("currency", {}).get("code")
    except (AttributeError, TypeError, ValueError):
        print("Ошибка в данных")
        return None

    if currency == "RUB":
        return amount

    load_dotenv()
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": os.getenv("API_KEY")}
    payload: Dict[str, Any] = {}

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return float(response.json()["result"])
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None
