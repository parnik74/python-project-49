from .brain_games import user_name, welcome_user
import prompt
import random


def prime(number):
    d = 2
    while number % d != 0:
        d += 1
    if d == number:
        return 'yes'
    else:
        return 'no'


def ask_user():
    correct_answers = 0
    while correct_answers < 3:
        number_1 = random.randint(1, 25)
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        answer = prompt.string(f"Question: {number_1} ")
        correct_answer = str(prime(number_1))
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is a wrong answer ;(. Correct answer was '{correct_answer}')"
            )
            correct_answers = 0
    print(f"Cogratulations! {user_name}")


def main():
    welcome_user()
    ask_user()


if __name__ == "__main__":
    main()
