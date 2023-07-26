from random import randint
from brain_games.engine import play


START_NUMBER = 1
END_NUMBER = 100
QUESTIONS_COUNT = 3


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    else:
        return gcd(b % a, a)


def round_generate():
    number_1 = randint(START_NUMBER, END_NUMBER)
    number_2 = randint(START_NUMBER, END_NUMBER)
    question = f'{number_1} {number_2}'
    correct_answer = str(gcd(number_1, number_2))

    return [question, correct_answer]


def main():
    description = 'Find the greatest common divisor of given numbers.'
    play(round_generate, description)
