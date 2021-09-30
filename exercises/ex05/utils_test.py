"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730383737"


def test_only_evens_none() -> None:
    """Edge Case: empty list."""
    x: list[int] = [1, 5, 7]
    assert only_evens(x) == []


def test_only_evens_both() -> None:
    """Use case: evens and odds."""
    x: list[int] = [1, 2, 3]
    assert only_evens(x) == [2]


def test_only_evens() -> None:
    """Use case: only events."""
    x: list[int] = [4, 4, 4]
    assert only_evens(x) == [4, 4, 4]


def test_sub_greater_end() -> None:
    """Edge Case: end index greater than length."""
    x: list[int] = [10, 20, 30, 40]
    begin: int = 1
    end: int = 5
    assert sub(x, begin, end) == [20, 30, 40]


def test_sub_middle() -> None:
    """Use Case: begining to 3rd index."""
    x: list[int] = [10, 20, 30, 40]
    begin: int = 0
    end: int = 3
    assert sub(x, begin, end) == [10, 20, 30]


def test_sub_all() -> None:
    """Use Case: begining to end index."""
    x: list[int] = [10, 20, 30, 40, 50, 60, 70]
    begin: int = 0
    end: int = 7
    assert sub(x, begin, end) == [10, 20, 30, 40, 50, 60, 70]


def test_concat_empty_list() -> None:
    """Concat with empty list."""
    list_1: list[int] = []
    list_2: list[int] = [2, 4, 6, 8, 10]
    assert concat(list_1, list_2) == [2, 4, 6, 8, 10]


def test_concat_evens() -> None:
    """Use case: only even numbers."""
    list_1: list[int] = [2, 8, 14, 68]
    list_2: list[int] = [46, 32, 4]
    assert concat(list_1, list_2) == [2, 8, 14, 68, 46, 32, 4]


def test_concat_big() -> None:
    """Use Case: large numbers."""
    list_1: list[int] = [2344, 2893, 32095]
    list_2: list[int] = [234, 58043, 4289]
    assert concat(list_1, list_2) == [2344, 2893, 32095, 234, 58043, 4289]