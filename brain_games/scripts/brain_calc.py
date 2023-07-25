from ..cli import welcome_user
import prompt
from random import randint, choice


name = welcome_user()
print('What is the result of the expression?')


def calculate(number_1, number_2, operation):
    match operation:
        case '+':
            return number_1 + number_2
        case '-':
            return number_1 - number_2
        case _:
            return number_1 * number_2

math_signs = ['+', '-', '*']
start_number = 1
end_number = 100


def main():
    count = 1
    questions_count = 3
    complete = False

    while count <= questions_count:
        operation = choice(math_signs)
        number_1 = randint(start_number, end_number)
        number_2 = randint(start_number, end_number)
        print(f'Question: {number_1} {operation} {number_2}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = calculate(number_1, number_2, operation)

        if int(user_answer) == correct_answer:
            print('Corect!')

            complete = count >= questions_count
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
