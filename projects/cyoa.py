"""Choose Your Own Adventure!"""

__author__ = 730383737

import random

# Emojis (6.1)
ATTACK = "\U0001F525"
CATCH = "\U00002728"
END_GAME = "\U0000274C"
EEVEE_TYPE = "\U00002734"
RAYQUAZA_TYPE_1 = "\U00002708"
RAYQUAZA_TYPE_2 = "\U000026E9"
METAGROSS_TYPE_1 = "\U0000269B"
METAGROSS_TYPE_2 = "\U000026D3"

#  Other named constants
ROCKET_BASE = 4


def main() -> None:
    """Pókemon Simulator!"""
    global points  # Global Variables (0)
    points = 0
    global player
    player = ""
    round: int = 1
    greet()
    
    while round >= 1:  # Game Loop (5)
        print(f"\nROUND {round}!")
        print("What would you like to do?")
        print(f"a. Catch {CATCH}")
        print(f"b. Attack {ATTACK}") 
        print(f"c. End. {END_GAME}")
        action_1 = input("Choose one: ")

        if action_1 == "a":  # Custom Procedure (3)
            print("\nYou look around and see three different pókemon: \na. Eevee \nb. Rayquaza \nc. Metagross")
            action_2 = input("Choose 1: ")

            if action_2 == "a":
                print(f"\nCongratulations {player}, you caught an Eevee! {EEVEE_TYPE}")
                evolution = input("Would you like to try for an eeveelution? Type yes or no: ")
                if evolution == "yes":
                    eeveelution_chance = random.randint(1, 8)
                    if eeveelution_chance == 1:
                        print("\nYour Eeeve evolved into a Jolteon!")
                    elif eeveelution_chance == 2:
                        print("\nYour Eeeve evolved into a Flareon!")
                    elif eeveelution_chance == 3:
                        print("\nYour Eeeve evolved into an Umbreon!")
                    elif eeveelution_chance == 4:
                        print("\nYour Eeeve evolved into a Leafeon!")
                    elif eeveelution_chance == 5:
                        print("\nYour Eeeve evolved into a Sylveon!")
                    elif eeveelution_chance == 6:
                        print("\nYour Eeeve evolved into a Glaceon!")
                    elif eeveelution_chance == 7:
                        print("\nYour Eeeve evolved into an Espeon!")
                    elif eeveelution_chance == 8:
                        print("\nYour Eeeve evolved into a Vaporeon!")
                    points = points + 1

            elif action_2 == "b":
                print(f"\nCongratulations {player}, you caught a Rayquaza! {RAYQUAZA_TYPE_1}{RAYQUAZA_TYPE_2}")
            elif action_2 == "c":
                print(f"\nCongratulations {player}, you caught a Metagross! {METAGROSS_TYPE_1}{METAGROSS_TYPE_2}")
            points = points + 1
            print(f"Total number of pókemon caught: {points}")

        elif action_1 == "b":  # Custom Function (4)
            print(f"\nGO Rocket Grunt: Let's rock and roll! \nOh no {player}! Team GO Rocket has captured a Tyranitar!")
            print("PS: Sucessfully caught Shadow pókemon count as 2 creatures!")
            rocket_attack = input("Type 'attack' to attack, or type 'run away' to leave this battle: ")

            if rocket_attack == "attack":
                points = team_rocket(points)
                print(f"Total number of pókemon caught: {points}")
            elif rocket_attack == "run away":
                print("\nGO Rocket Grunt: Team GO Rocket always wins!")
                print(f"Total number of pókemon caught: {points}")

        elif action_1 == "c":
            print(f"\nThank you for playing {player}!")
            print(f"You caught {points} pokemon")
            print("END OF GAME")
            break

        elif action_1 != "a" and action_1 != "b" and action_1 != "c":
            print("Sorry I didn't understand. Please try again.")
            continue
        round = round + 1 


def greet() -> None:
    """Greets the player."""
    print("Hello Trainer, welcome to Pókemon Spawn! Here you'll have the chance to catch and battle different pókemon")
    print("Simply type the letter corresponding to which action you want to do.")
    print("Once you're done, you'll be able to see how many creatures you sucessfully caught!")
    global player
    player = input("To begin, what is your name? ")
    print(f"\nGood luck {player}, and be on the lookout for Team GO Rocket!")


def team_rocket(points_local: int) -> int:
    """Results in a random integer to 'defeat' Team Rocket."""
    trainer_base = random.randint(0, 10)  # (6.2)
    print(f"\n{player} attack: {trainer_base} \nTeam Rocket defense: {ROCKET_BASE}")

    if trainer_base > ROCKET_BASE:
        print(f"\nCongratulations {player}! You caught a shadow Tyranitar!")
        points_local = points_local + 2
        return points_local
    else:
        print(f"\nGO Rocket Grunt: Team GO Rocket always wins! \nSorry {player}, Team Rocket won this round.")
        return points_local


if __name__ == "__main__":  # main (1)
    main()