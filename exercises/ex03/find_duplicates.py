"""Finding duplicate letters in a word."""

<<<<<<< HEAD
__author__ = "730383737"

word: str = (input("Enter a word: "))
i = 0
counter_two = 0
duplicates = 0

while i < len(word):
    counter_two = i + 1
    while counter_two < len(word):
        if word[i] == word[counter_two]:
            duplicates = duplicates + 1
            counter_two = counter_two + 1
        else:
            counter_two = counter_two + 1
    i = i + 1
        
variable = str(duplicates > 0)
print(duplicates)
print("Found duplicate: " + variable)
=======
__author__ = "123456789"

word: str = input("Enter a word: ")

i: int = 0
duplicate: bool = False
while (i < len(word)):
    j: int = i + 1
    while(j < len(word)):
        if (word[i] == word[j]):
            duplicate = True
        j += 1
    i += 1

print("Found duplicate: " + str(duplicate))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
