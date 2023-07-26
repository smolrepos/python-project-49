from brain_games.engine import play
from random import randint


PROGRESSION_LENGTH = 10


def gen_progression():
    step = randint(1, 20)
    number = randint(1, 100)
    count = 1
    progression = []
    while count <= PROGRESSION_LENGTH:
        progression.append(str(number))
        number += step
        count += 1
    return progression


def get_round_entries(progression):
    step_num = randint(0, PROGRESSION_LENGTH - 1)
    previous_index = step_num
    correct_answer = progression.pop(step_num)
    progression.insert(previous_index, '..')
    question = ' '.join(progression)
    return question, str(correct_answer)


def round_generate():
    progression = gen_progression()
    return get_round_entries(progression)


def main():
    description = 'What number is missing in the progression?'
    play(round_generate, description)
