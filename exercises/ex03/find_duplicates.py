"""Finding duplicate letters in a word."""

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