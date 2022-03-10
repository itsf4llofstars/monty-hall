#!/usr/bin/env python3
"""main.py"""
import random
import secrets

# GLOBALS
WIN_LOSS = [False, True]
DOORS = [None, None, None]


def set_winning_door():
    """Picks one winning door and two losing doors"""
    door = secrets.randbelow(3)
    DOORS[door] = True
    if DOORS[0] is not None:
        DOORS[1] = not DOORS[0]
        DOORS[2] = not DOORS[0]
    elif DOORS[1] is not None:
        DOORS[0] = not DOORS[1]
        DOORS[2] = not DOORS[1]
    elif DOORS[2] is not None:
        DOORS[0] = not DOORS[2]
        DOORS[1] = not DOORS[2]

    for _ in range(1000):
        random.shuffle(DOORS)


def get_users_choice():
    """Get contestants door choice"""
    users_choice = 0
    while 0 < users_choice < 4:
        users_choice: int = int(input("Enter your choice of doors (1, 2, 3): "))
        if not 0 < users_choice < 4:
            print("\nPlease pick a number of 1, 2, or 3\n")
    return users_choice


def pick_show_door():
    """Chooses which losing door to show"""
    pass


def main():
    """main function"""
    set_winning_door()
    choosen_door = get_users_choice()
    print(choosen_door)


if __name__ == "__main__":
    from os import system
    from sys import exit

    system("clear")
    exit(main())
