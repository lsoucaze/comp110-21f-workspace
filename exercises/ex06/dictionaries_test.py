"""Unit tests for dictionary functions."""

# python -m pytest exercises/ex06

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730383737"


def test_invert_cats() -> None:
    """Edge case: single entry."""
    set_1 = {'apple': 'cat'}
    assert invert(set_1) == {'cat': 'apple'}


def test_invert_full_list() -> None:
    """Use case: complex list."""
    set_1 = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(set_1) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_small_list() -> None:
    """Use case: small list."""
    set_1 = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
    assert invert(set_1) == {'red': 'apple', 'yellow': 'banana', 'purple': 'grape'}


def test_favorite_color_same() -> None:
    """Edge case: Equal colors."""
    color_dict = {'Lilly': 'Pink', 'Marc': 'Red', 'Ezri': 'Blue', 'Kris': 'Blue', 'Chris': 'Red'}
    assert favorite_color(color_dict) == "Red"


def test_favorite_color_simple() -> None:
    """Use case: three entries."""
    color_dict = {'Marc': 'Yellow', 'Ezri': 'Blue', 'Kris': 'Blue'}
    assert favorite_color(color_dict) == "Blue"


def test_favorite_color_complex() -> None:
    """Use case: simple five entries."""
    color_dict = {'Marc': 'Yellow', 'Ezri': 'Blue', 'Kris': 'Blue', 'Chris': 'Yellow', 'James': 'Blue'}
    assert favorite_color(color_dict) == "Blue"


def test_count_complex() -> None:
    """Edge case: no repeating entires."""
    input_list = ["apple", "banana", "pear", "orange", "grape"]
    assert count(input_list) == {'apple': 1, 'banana': 1, 'pear': 1, 'orange': 1, 'grape': 1}


def test_count_simple() -> None:
    """Use case: some repeating entires."""
    input_list = ["apple", "banana", "apple", "orange", "apple"]
    assert count(input_list) == {'apple': 3, 'banana': 1, 'orange': 1}


def test_count_long() -> None:
    """Use case: a lot of repeating entires."""
    input_list = ["apple", "banana", "apple", "orange", "apple", "apple", "grape", "grape", "orange", "banana"]
    assert count(input_list) == {'apple': 4, 'banana': 2, 'orange': 2, 'grape': 2}