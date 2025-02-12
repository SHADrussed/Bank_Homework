import pytest

from src.processing import sort_by_date

@pytest.mark.parametrize("input_data, reverse, expected_output", [
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ],
        True,  # Указываем reverse=True для сортировки по убыванию
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]
    ),
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ],
        False,  # Указываем reverse=False для сортировки по возрастанию
        [
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
        ]
    ),
    (
        [
            {'id': 123456789, 'state': 'EXECUTED', 'date': '2020-01-01T00:00:00'},
            {'id': 987654321, 'state': 'CANCELED', 'date': '2020-01-01T00:00:00'},
            {'id': 555555555, 'state': 'PENDING', 'date': '2020-01-01T00:00:00'}
        ],
        False,
        [
            {'id': 123456789, 'state': 'EXECUTED', 'date': '2020-01-01T00:00:00'},
            {'id': 987654321, 'state': 'CANCELED', 'date': '2020-01-01T00:00:00'},
            {'id': 555555555, 'state': 'PENDING', 'date': '2020-01-01T00:00:00'}
        ]
    ),
    (
        [
            {'id': 11111111, 'state': 'EXECUTED', 'date': '2020-13-32T25:61:59'},  # Некорректная дата
            {'id': 22222222, 'state': 'CANCELED', 'date': '2020-01-01T00:00:00'},
            {'id': 33333333, 'state': 'PENDING', 'date': '2020-01-01T00:00:00'}
        ],
        False,
        [
            {'id': 22222222, 'state': 'CANCELED', 'date': '2020-01-01T00:00:00'},
            {'id': 33333333, 'state': 'PENDING', 'date': '2020-01-01T00:00:00'},
            {'id': 11111111, 'state': 'EXECUTED', 'date': '2020-13-32T25:61:59'}  # Ожидается исключение или другое поведение
        ]
    ),
    (
        [
            {'id': 44444444, 'state': 'EXECUTED', 'date': '31/12/2020 23:59:59'},  # Нестандартный формат даты
            {'id': 55555555, 'state': 'CANCELED', 'date': '2020-01-01T00:00:00'},
            {'id': 66666666, 'state': 'PENDING', 'date': '2020-01-01T00:00:00'}
        ],
        False,
        [
            {'id': 55555555, 'state': 'CANCELED', 'date': '2020-01-01T00:00:00'},
            {'id': 66666666, 'state': 'PENDING', 'date': '2020-01-01T00:00:00'},
            {'id': 44444444, 'state': 'EXECUTED', 'date': '31/12/2020 23:59:59'}  # Ожидается исключение или другое поведение
        ]
    )
])

def test_sort_by_date(input_data, reverse, expected_output):
    assert sort_by_date(input_data, reverse) == expected_output
