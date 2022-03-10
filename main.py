#!/usr/bin/env python3
"""main.py"""
import random
import secrets

# GLOBALS
WIN_LOSS = [False, True]
DOORS = [None, None, None]


def set_winning_door():
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

    print(DOORS)
    for _ in range(1000):
        random.shuffle(DOORS)
    print(DOORS)


def main():
    """main function"""
    set_winning_door()


if __name__ == "__main__":
    from os import system
    from sys import exit

    system("clear")
    exit(main())
