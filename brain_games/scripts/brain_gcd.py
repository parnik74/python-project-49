from .brain_games import user_name, welcome_user
import prompt
import random


def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n


def ask_user():
    correct_answers = 0
    while correct_answers < 3:
        number_1 = random.randint(1, 25)
        number_2 = random.randint(1, 25)
        print("Find the greatest common divisor of given numbers.")
        answer = prompt.string(f"Question: {number_1} {number_2} ")
        correct_answer = str(gcd(number_1, number_2))
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
