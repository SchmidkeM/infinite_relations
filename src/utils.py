import inspect

def compare_lists_orderless(list: list, list2: list):
    return len(list) == len(list2) and all(item in list2 for item in list)

def flatten_list(list_of_lists: list):
    return [item for sublist in list_of_lists for item in sublist]

def dict_from_lists(keys: list, values: list):
    return {keys[i]: values[i] for i in range(len(keys))}

def get_parameter_names(fun: callable):
    return inspect.getfullargspec(fun)[0]