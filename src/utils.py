import json


def get_list_dict_transactions(the_way):
    try:
        with open(the_way, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        return []
