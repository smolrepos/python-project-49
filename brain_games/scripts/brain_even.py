from ..cli import welcome_user
import prompt
from random import randint


name = welcome_user()
print('Answer "yes" if the number is even, otherwise answer "no".')


def parity_check(numeric):
    if numeric % 2 == 0:
        return 'yes'
    return 'no'


def main():
    count = 1
    questions_count = 3
    complete = False

    while count <= questions_count:
        number = randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = parity_check(number)

        if user_answer == correct_answer:
            print('Correct!')

            complete = count >= questions_count
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correnct answer was '{correct_answer}'.)\nLet's try again, {name}!")
            break

    if complete:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()