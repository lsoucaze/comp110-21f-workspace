"""Practice with dictionaries."""

__author__ = "730383737"


def invert(set_1: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    set_2 = dict()  # New flipped list
    
    for key in set_1:
        if set_1[key] in set_2:
            raise KeyError
        else:
            set_2[set_1[key]] = key
    
    return set_2


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the color that occurs most frequently."""
    color_dict = dict()
    color: str = ""

    for x in input_dict:

        if input_dict[x] in color_dict:  # if the value is in the list, then it's a duplicate
            color_dict[input_dict[x]] += 1
        else:
            color_dict[input_dict[x]] = 1

    i: int = 0

    for c in color_dict:
        if color_dict[c] > i:
            i = color_dict[c]
            color = c

    return color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts how frequent a value appears in a list."""
    final_set = dict()
    
    for fruit in input_list:  # I use fruit in tests. It makes sense I promise.
        if fruit in final_set:
            final_set[fruit] += 1
        else:
            final_set[fruit] = 1
        
    return final_set