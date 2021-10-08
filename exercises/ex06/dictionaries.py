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


def favorite_color(color_list: dict[str, str]) -> str:
    """Returns the color that occurs most frequently."""
    color: str = ""
    color_count: int = 0
    color_count_2: int = 0

    for x in color_list:
        color = color_list[x]

        if color_list[x] == color:
            color_count += 1
        else:
            color_count_2 += 1
            color_2 = x

    if color_count >= color_count_2:
        return color
    if color_count <= color_count_2:
        return color_list[color_2]


def count(input_list: list[str]) -> dict[str, int]:
    final_set = dict()
    
    for fruit in input_list:  # I use fruit in tests. It makes sense I promise.
        if fruit in final_set:
            final_set[fruit] += 1
        else:
            final_set[fruit] = 1
        
    return final_set


input_list = ["apple", "banana", "apple"]
print(count(input_list))