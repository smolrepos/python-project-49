import prompt
from brain_games.cli import welcome_user


def play(round_generate, description):
    QUESTIONS_COUNT = 3
    name = welcome_user()
    count = 1
    complete = False

    print(description)

    while count <= QUESTIONS_COUNT:
        question, correct_answer = round_generate()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Corect!')

            complete = count >= QUESTIONS_COUNT
            count += 1
        else:
            print(f'Question: {question}\nYour answer: {user_answer}')
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if complete:
        print(f'Congratulations, {name}!')