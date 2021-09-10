"""Drawing forests in a loop."""

__author__ = "730383737"

# The string constant for the pine tree emoji

TREE: str = '\U0001F332'
TREE_2 = TREE
counter: int = 0
depth = int(input("Depth: "))

if counter < depth:
    while counter < depth:
        print(TREE)
        TREE = TREE + TREE_2
        counter = counter + 1