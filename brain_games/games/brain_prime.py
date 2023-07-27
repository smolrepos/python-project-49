from random import randint
from brain_games.engine import play


START_NUMBER = 1
END_NUMBER = 100


def is_prime(number):
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    if number % 3 == 0:
        return number == 3
    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def round_generate():
    question = randint(START_NUMBER, END_NUMBER)
    correct_answer = 'yes' if is_prime(question) else 'no'

    return [question, correct_answer]


def main():
    description = 'Answer "yes" if given number' \
        ' is prime. Otherwise answer "no".'
    play(round_generate, description)
