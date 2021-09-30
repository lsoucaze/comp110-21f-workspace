"""List utility functions part 2."""

__author__ = "730383737"


def only_evens(a_list: list[int]) -> list[int]:
    """Given a list of integers, return only the even ones."""
    i: int = 0
    even_list: list[int] = []
    while i < len(a_list):
        if a_list[i] % 2 == 0:
            even_list.append(a_list[i])
        i += 1
    return even_list


def sub(x: list[int], begin: int, end: int) -> list[int]:
    """Generates a subset list based on a given list, a start, and an end index."""
    list_2: list[int] = []
    if begin < 0:
        begin = 0
    if end > len(x):
        end = len(x)
    if len(x) == 0 or begin > len(x) or end <= 0:
        return list_2 

    while begin < end:
        list_2.append(x[begin])
        begin += 1
    return list_2


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Combines the content of two lists into a new list."""
    list_3: list[int] = []
    i: int = 0

    while i < len(list_1):
        list_3.append(list_1[i])
        i += 1
    
    i = 0

    while i < len(list_2):
        list_3.append(list_2[i])
        i += 1

    return list_3