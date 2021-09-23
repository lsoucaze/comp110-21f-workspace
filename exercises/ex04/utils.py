"""List utility functions."""

__author__ = "730383737"


def all(haystack: list[int], needle: int) -> bool:
    """Indicates whether or not all the ints in the list are the same as the given int."""
    i: int = 0

    if len(haystack) == 0:
        return False
    while i < len(haystack):
        item: int = haystack[i]
        if item != needle:
            return False
        i += 1

    return True


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Indicates whether 2 lists of int values are identical at every index value."""
    i: int = 0

    if len(list_1) == len(list_2):
        while i < len(list_1):
            if list_1[i] != list_2[i]:
                return False
            i += 1
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """Returns the max value of the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    i: int = 0
    value: int = input[0]
    
    while i < len(input):
        if input[i] >= value:
            value: int = input[i]
        i += 1
    return value