"""Utility functions."""

__author__ = "730383738"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done to  free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-orientated table to a column-orientated table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(data: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returns the first few rows from a larger table of data."""
    result: dict[str, list[str]] = {}

    for column in data:
        headers: list[str] = []

        i = 0
        if rows > len(data[column]):
            while i < len(data):
                headers.append(data[column][i])
                i += 1
        else: 
            while i < rows:
                headers.append(data[column][i])
                i += 1
        result[column] = headers
    return result


def select(data: dict[str, list[str]], input: list[str]) -> dict[str, list[str]]:
    """Returns a subset of the original data."""
    result: dict[str, list[str]] = {}

    for column in input:
        result[column] = data[column]

    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables into one."""
    result: dict[str, list[str]] = {}
    
    for column_1 in table_1:
        result[column_1] = table_1[column_1]

    for column_2 in table_2:
        if column_2 in result:
            result[column_2] += table_2[column_2]
        else:
            result[column_2] = table_2[column_2]

    return result


def count(input: list[str]) -> dict[str, int]:
    """Returns the frequency of a value."""
    result: dict[str, int] = {}
    
    for key in input:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    
    return result


def cs_course_response(subset: dict[str, list[str]], word: str) -> dict[str, list[str]]:
    """Filters dictionary based on responses."""
    results: dict[str, list[str]] = {}
    results["AP_A"] = []
    results["AP_Principles"] = []
    results["difficulty"] = []
    
    for i in range(len(subset["AP_A"])):
        if subset["AP_A"][i] == "Yes" or subset["AP_Principles"][i] == "Yes":
            results["AP_A"].append(subset["AP_A"][i])
            results["AP_Principles"].append(subset["AP_Principles"][i])
            results["difficulty"].append(subset["difficulty"][i])

    return results
