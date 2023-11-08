#!/usr/bin/env python3

import prompt
print("Welcome to the Brain Games!")
user_name = prompt.string('May I have your name? ')


def main():
    welcome_user()


def welcome_user():
    print(f"Hello, {user_name}!")


if __name__ == "__main__":
    main()
