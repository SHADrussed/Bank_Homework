import pytest

from src.processing import filter_by_state


@pytest.mark.parametrize('user_data, state, expected', [
    # Фильтрация по умолчанию (EXECUTED)
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ],
        "EXECUTED",
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]
    ),
    # Фильтрация по состоянию CANCELED
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ],
        "CANCELED",
        [
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    ),
    # Пустой список на входе
    (
        [],
        "EXECUTED",
        []
    ),
    # Нет элементов с указанным состоянием
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ],
        "CANCELED",
        []
    ),
    # Отсутствие ключа 'state' в некоторых элементах
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},  # Нет ключа 'state'
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
        ],
        "EXECUTED",
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
        ]
    ),
    # Все элементы без ключа 'state'
    (
        [
            {'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'}
        ],
        "EXECUTED",
        []
    ),
])

def test_filter_by_state(user_data, state, expected):
    assert filter_by_state(user_data, state) == expected