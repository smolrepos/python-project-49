import prompt
from random import randint, choice
from ..cli import welcome_user
from brain_games.scripts.config import brain_calc as config


name = welcome_user()
OPERATIONS = config.OPERATIONS
START_NUMBER = 1
END_NUMBER = 100
QUESTIONS_COUNT = 3
print('What is the result of the expression?')


def calculate(number_1, number_2, operation):
    match operation:
        case config.MATH_ADD:
            return number_1 + number_2
        case config.MATH_SUB:
            return number_1 - number_2
        case config.MATH_MUL:
            return number_1 * number_2
        case _:
            raise Exception(f'Wrong operation "{operation}".  Supported operation - {", ".join(OPERATIONS)}.')


def main():
    count = 1
    complete = False

    while count <= QUESTIONS_COUNT:
        operation = choice(OPERATIONS)
        number_1 = randint(START_NUMBER, END_NUMBER)
        number_2 = randint(START_NUMBER, END_NUMBER)
        print(f'Question: {number_1} {operation} {number_2}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = calculate(number_1, number_2, operation)

        if int(user_answer) == correct_answer:
            print('Corect!')

            complete = count >= QUESTIONS_COUNT
            count += 1
        else:
            print(f'Question: {number_1} {operation} {number_2}\nYour answer: {str(correct_answer)}')
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if complete:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
