from brain_games.engine import play
import prompt
from random import randint


def get_answer(numeric):
    if numeric % 2 == 0:
        return 'yes'
    return 'no'


def round_generate():
    question = randint(1, 100)
    correct_answer = get_answer(question)

    return [question, correct_answer]


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    play(round_generate, description)


if __name__ == '__main__':
    main()
