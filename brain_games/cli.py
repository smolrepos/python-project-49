from __future__ import print_function
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
