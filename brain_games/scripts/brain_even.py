from .brain_games import *
import prompt
import random


def ask_user():
    correct_answers = 0
    while correct_answers < 3:
      number = random.randint(0,50)
      print(number)
      answer = prompt.string('Answer "yes" if the number is even, otherwise answer "no".')
      if answer == 'yes' and (number % 2) == 0:
        correct_answers += 1
        print('Correct!')
      elif answer == 'no' and (number % 2) != 0:
        correct_answers += 1
        print('Correct!')
      elif answer == 'no' and (number % 2) == 0:
        correct_answers = 0
        print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {user_name}!")
      elif answer == 'yes' and (number % 2) != 0:
        correct_answers = 0
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {user_name}!")
      else:
         print(f"\nWrong answer ;(. \nLet's try again, {user_name}!")
    print(f"Congratulations, {user_name}!")


def main():
    # print("Welcome to the Brain Games!")
    welcome_user()
    ask_user()
    

if __name__ == "__main__":
    main()
