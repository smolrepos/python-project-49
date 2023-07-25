from ..cli import welcome_user
import prompt
from random import randint, choice


name = welcome_user()
print('What is the result of the expression?')


def verification_expression(number_1, random_math_sign1, number_2):
  if random_math_sign1 == '+':
    total = number_1 + number_2
  elif random_math_sign1 == '-':
    total = number_1 - number_2
  else:
    total = number_1 * number_2
  return total


def main():
    count = 1
    questions_count = 3

    while count <= questions_count:
        math_signs = ['+', '-', '*']
        random_math_sign = choice(math_signs)
        number1 = randint(1, 100)
        number2 = randint(1, 15)
        print(f'Question: {number1} {random_math_sign} {number2}')
        user_answer = prompt.string('Your answer: ')
        correct_answer_to_expression = verification_expression(number1, random_math_sign, number2)

        if user_answer == str(correct_answer_to_expression):
            print('Corect!')

            complete = count >= questions_count
            count += 1
        else:
            print(f'Question: {number1} {random_math_sign} {number2}\nYour answer: {str(correct_answer_to_expression)}')
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer_to_expression}'.")
            print(f"Let's try again, {name}!")
            break

    if complete:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
