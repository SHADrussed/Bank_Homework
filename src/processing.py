def filter_by_state(list_of_kwargs, state = 'EXECUTED'):
    new_list_kwargs = []
    for i in list_of_kwargs:
        if i['state'] == state:
            new_list_kwargs.append(i)
    return new_list_kwargs