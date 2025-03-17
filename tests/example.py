from src.external_api import get_amount_of_transaction
from src.utils import get_list_dict_transactions

print(get_amount_of_transaction({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "USD"
      }
    }
}
))

print(get_amount_of_transaction({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58"
      }
}
))

print(get_list_dict_transactions(r'D:\PythonProjects\Bank_Homework\data\operations.json'))
print(get_list_dict_transactions(r'Dвдаж'))