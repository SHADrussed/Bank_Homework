import json
from typing import List, Dict, Any, cast


def get_list_dict_transactions(the_way: str) -> List[Dict[str, Any]]:
    try:
        with open(the_way, "r", encoding="utf-8") as file:
            data = json.load(file)
            return cast(List[Dict[str, Any]], data)
    except Exception:
        return []
