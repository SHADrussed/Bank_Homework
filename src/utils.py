import json
import logging
from typing import List, Dict, Any, cast

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def get_list_dict_transactions(the_way: str) -> List[Dict[str, Any]]:
    try:
        with open(the_way, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info(f"Успешно загружены данные из файла {the_way}")
            return cast(List[Dict[str, Any]], data)
    except Exception as e:
        logger.error(f"Ошибка при загрузке данных из файла {the_way}: {e}")
        return []


# Пример использования функции
if __name__ == "__main__":
    transactions = get_list_dict_transactions("transactions.json")
    print(transactions)
