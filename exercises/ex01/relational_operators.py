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