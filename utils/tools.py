def switch_case(value, case:list, result:list, mode = lambda a,b:a<b):
    """
    Use like a C/C++/Java switch cas.
    :param value : is the value to test.
    :param case  : list of case value
    :param result: list of result of each case
    :param mode  : functon or lambda to use on every case.
    :return: the reslut[i] where mode(value, case[i]) == True
    """
    for i, val in enumerate(case):
        if mode(value, val):
            return result[i]


def switch_case_function(*args, **kwargs):
    """
    Use like a C/C++/java switch case but all result is function.
    :param args: see switch_case function.
    :param kwargs: see switch_case function.
    :return: return of result function.
    """
    return switch_case(*args, **kwargs)()
