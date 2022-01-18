def even_numb(some_dict):
    result_dict = dict()
    for key,value in some_dict.items():
        try:
            if some_dict[key] % 2 == 0:
                result_dict[key] = value
        except TypeError as err:
            return f'Значение словаря не число: {err}'
    return result_dict


def alfa(some_dict):
    result_dict = dict()
    for key,value in some_dict.items():
        try:
            if key.isalpha():
                result_dict[key.lower()] = value
        except AttributeError as err:
            return f'Ключ словаря не строка: {err}'
    return result_dict


def not_none(some_dict):
    result_dict = dict()
    for key, value in some_dict.items():
        if some_dict[key] is not None:
            result_dict[key] = value
    return result_dict
