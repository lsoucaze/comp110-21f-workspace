<<<<<<< HEAD
"""Practice with str, int, and numeric operations."""

__author__ = "730383737"


lside = int(input("Number variable 1? "))
rside = int(input("Number variable 2? "))
a = lside ** rside
b = lside / rside
c = lside // rside
d = lside % rside
lside = str(lside)
rside = str(rside)
print("Left-hand side: " + (lside))
print("Right-hand side: " + (rside))
print((lside) + " ** " + (rside) + " is " + str(a))
print((lside) + " / " + (rside) + " is " + str(b))
print((lside) + " // " + (rside) + " is " + str(c))
print((lside) + " % " + (rside) + " is " + str(d))
=======
"""Demonstrates python numeric operators for two input numbers."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " ** " + string_two + " is " + str(number_one ** number_two))
print(string_one + " / " + string_two + " is " + str(number_one / number_two))
print(string_one + " // " + string_two + " is " + str(number_one // number_two))
print(string_one + " % " + string_two + " is " + str(number_one % number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
