"""Drawing forests in a loop."""

__author__ = "730383737"

# The string constant for the pine tree emoji
<<<<<<< HEAD

TREE: str = '\U0001F332'
TREE_2 = TREE
counter: int = 0
depth = int(input("Depth: "))

if counter < depth:
    while counter < depth:
        print(TREE)
        TREE = TREE + TREE_2
        counter = counter + 1
=======
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))

i: int = 0
duplicate: bool = False
while (i < depth):
    j: int = 0
    tree: str = ""
    while(j < i + 1):
        tree += TREE
        j += 1
    print(tree)
    i += 1
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
