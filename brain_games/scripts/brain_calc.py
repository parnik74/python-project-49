from .brain_games import user_name, welcome_user
import prompt
import random


def check_math(x, number_1, number_2):
    if x == "+":
        result = number_1 + number_2
    elif x == "-":
        result = number_1 - number_2
    else:
        result = number_1 * number_2
    return result


def ask_user():
    correct_answers = 0
    while correct_answers < 3:
        operators = ["+", "-", "*"]
        random_operator = random.choice(operators)
        number_1 = random.randint(0, 10)
        number_2 = random.randint(0, 10)
        answer = prompt.string(f"Question: {number_1} {random_operator} {number_2} ")
        result = check_math(random_operator, number_1, number_2)
        result_as_string = str(result)
        if answer == result_as_string:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"\n'{answer}' is wrong answer ;(. Correct answer was '{result}'\nLet's try again, {user_name}!"
            )
            correct_answers = 0
    print(f"Congratulations, {user_name}!")


def main():
    welcome_user()
    ask_user()


if __name__ == "__main__":
    main()
