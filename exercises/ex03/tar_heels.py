"""An exercise in remainders and boolean logic."""

__author__ = "730383737"


# Begin your solution here...

number = int(input("Enter an int: "))

if number % 2 == 0 or number % 7 == 0:  # must be divs. by 2 or 7
    if not(number % 2 == 0 and number % 7 == 0):  # not divis. by both
        if not number % 7 == 0:  # divis. only by 7
            print("TAR")  
        else:  # divis. only by 2
            print("HEELS")
    else:  # divis. by 2 AND 7
        print("TAR HEELS")

else:  # not divis.
    print("CAROLINA")