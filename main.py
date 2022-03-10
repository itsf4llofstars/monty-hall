#!/usr/bin/env python3
"""main.py"""
import secrets


def say_hi(the_name) -> str:
    return f"Hello {the_name.title()}"


def main():
    """main function"""
    name: str = "darren"
    greeting: str = say_hi(name)
    print(greeting)


if __name__ == "__main__":
    from os import system
    from sys import exit

    system("clear")
    exit(main())
