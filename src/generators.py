def filter_by_currency(list_of_dict, currency):
    return list(filter(lambda x: x.get("operationAmount", {}).get("currency", {}).get("name") == currency, list_of_dict))

def transaction_descriptions(list_of_dict, start=1):
    while True:
        yield list_of_dict
        start+=1
    pass

def card_number_generator(floor, ceiling):
    return [str(i).zfill(16) for i in range(floor, ceiling)]