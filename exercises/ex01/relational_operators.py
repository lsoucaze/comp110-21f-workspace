<<<<<<< HEAD
"""Practice with str, int, and operations."""

__author__ = "730383737"


lside: str = input("Number variable 1? ")
rside: str = input("Number variable 2? ")
lsint = int(lside)
rsint = int(rside)
a = str(lsint < rsint)
b = str(lsint >= rsint)
c = str(lsint == rsint)
d = str(lsint != rsint)
print("Left-hand side: " + lside)
print("Right-hand side: " + rside)
print(lside + " < " + rside + " is " + a)
print(lside + " >= " + rside + " is " + b)
print(lside + " == " + rside + " is " + c)
print(lside + " != " + rside + " is " + d)
=======
"""Demonstrates python relational operators for two number inputs."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " < " + string_two + " is " + str(number_one < number_two))
print(string_one + " >= " + string_two + " is " + str(number_one >= number_two))
print(string_one + " == " + string_two + " is " + str(number_one == number_two))
print(string_one + " != " + string_two + " is " + str(number_one != number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
