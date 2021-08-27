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