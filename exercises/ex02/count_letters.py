"""Counting letters in a string."""

<<<<<<< HEAD
__author__ = "730383737"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1


# Begin your solution here...

<<<<<<< HEAD
letter: str = (input("What letter do you want to search for?: "))
word: str = (input("Enter a word: "))
i: int = 0
count: int = 0

while i < len(word): 
    if letter == word[i]:
        count = count + 1
        i = i + 1
    else:
        i = i + 1

print("Count: " + str(count))
=======
letter: str = input("What letter do you want to seach for? ")
word: str = input("Enter a word ")
count: int = 0
i: int = 0
while (i < len(word)):
    if word[i] == letter:
        count += 1
    i += 1
print("Count: " + str(count))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
