from typing import Any


def filter_by_state(list_of_kwargs, state='EXECUTED'):
    """Сортирует список по статусу"""
    new_list_kwargs: list[Any] = []
    for i in list_of_kwargs:
        if i['state'] == state:
            new_list_kwargs.append(i)
    return new_list_kwargs


def sort_by_date(operations, reverse=True):
    """Сортирует список словарей по дате."""
    return sorted(operations, key=lambda x: x['date'], reverse=reverse)
