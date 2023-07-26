from random import randint, choice
from brain_games.games.config import brain_calc as config
from brain_games.engine import play


OPERATIONS = config.OPERATIONS
START_NUMBER = 1
END_NUMBER = 100
QUESTIONS_COUNT = 3


def calculate(number_1, number_2, operation):
    match operation:
        case config.MATH_ADD:
            return number_1 + number_2
        case config.MATH_SUB:
            return number_1 - number_2
        case config.MATH_MUL:
            return number_1 * number_2
        case _:
            raise Exception(
                f'Wrong operation "{operation}". Supported operation - {", ".join(OPERATIONS)}.'
            )


def round_generate():
    operation = choice(OPERATIONS)
    number_1 = randint(START_NUMBER, END_NUMBER)
    number_2 = randint(START_NUMBER, END_NUMBER)
    question = f'{number_1} {operation} {number_2}'
    correct_answer = str(calculate(number_1, number_2, operation))

    return [question, correct_answer]


def main():
    description = 'What is the result of the expression?'
    play(round_generate, description)
