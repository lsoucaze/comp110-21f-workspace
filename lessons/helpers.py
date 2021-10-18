"""Define a powerful function used elsewhere."""


def main() -> None:
    """Entrypoint of our program."""
    print(f"helps.py: {__name__}")
    print(powerful(2, 10))


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


#  Idiomatic python: having a main function
if __name__ == "__main__":
    main()

#  You typically would not have an else statement here
#  else:
#      print("this module was imported")