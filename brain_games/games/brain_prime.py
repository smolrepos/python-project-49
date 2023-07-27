from random import randint
from brain_games.engine import play


START_NUMBER = 1
END_NUMBER = 100


def prime_number(number):
  if number == 0 or number == 1:
    return 'no'
  elif number == 2 or number == 3 or number == 5 or number == 11:
    return 'yes'
  elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
    return 'no'
  else:
    return 'yes'


def round_generate():
    question = randint(START_NUMBER, END_NUMBER)
    correct_answer = prime_number(question)

    return [question, correct_answer]



def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play(round_generate, description)
