from brain_games.engine import play
from random import randint


def gen_progression():
    step = randint(1, 20)
    number = randint(1, 100)
    count = 1
    progression = []
    while count <= 10:
        progression.append(str(number))
        number += step
        count += 1
    return progression


def get_round_entries(ls_2):
    step_num = randint(0, 9)
    previous_index = step_num
    correct_answer = ls_2.pop(step_num)
    ls_2.insert(previous_index, '..')
    progression = ' '.join(ls_2)
    return progression, correct_answer


def round_generate():
    final_progression, answer = get_round_entries(gen_progression())
    question = f'{final_progression}'
    correct_answer = str(answer)

    return [question, correct_answer]


def main():
    description = 'What number is missing in the progression?'
    play(round_generate, description)
