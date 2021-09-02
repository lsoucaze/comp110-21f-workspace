"""Repeating a beat in a loop."""

__author__ = "730383737"


# Begin your solution here...

beat = str(input("What beat do you want to repeat? "))
beat_2 = beat
rep = int((input("How many times do you want to repeat it? ")))
counter: int = 0

if rep <= counter:
    print("No beat...")

else:
    while counter < rep:
        final = beat + " " + beat_2
        counter = counter + 1
        
    print(str(final) + " " + beat_2)