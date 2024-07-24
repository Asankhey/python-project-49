#!/usr/bin/env python3
from brain_games.scripts.cli import welcome_user


def greet_hello():
    print('Welcome to the Brain Games!')


def main():
    greet_hello()
    welcome_user()


if __name__ == '__main__':
    main()
