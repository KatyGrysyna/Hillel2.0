def get_average(num):
    if not num:
        return 0
    return sum(num) / len(num)


def get_elements(list1, list2):
    return list(set(list1) & set(list2))
