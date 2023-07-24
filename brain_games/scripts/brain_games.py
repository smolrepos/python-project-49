#!/usr/bin/env python3
from ..cli import welcome_user


def greet(text):
    print(text)


def main():
    greet('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
