"""An exercise in remainders and boolean logic."""

<<<<<<< HEAD
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
=======
__author__ = "730243388"


# Begin your solution here...
num: int = int(input("Enter an int: "))

if (num % 14 == 0):
    print("TAR HEELS")
elif (num % 7 == 0):
    print("HEELS")
elif (num % 2 == 0):
    print("TAR")
else:
    print("CAROLINA")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
