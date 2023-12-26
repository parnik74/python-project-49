from .brain_games import user_name, welcome_user
import prompt
import random

def ask_user():
    correct_answers = 0
    while correct_answers < 3:
        range_of_sequence = random.randint(5, 10)
        range_of_addition = random.randint(1, 5)
        missing_sequence = random.randint(0, range_of_sequence - 1)
        array = []
        a = 1
        x = 0
        while x < range_of_sequence:
            array.append(a)
            a += range_of_addition
            x += 1
        correct_answer = str(array[missing_sequence])
        array[missing_sequence] = '..'
        array_as_string = ' '.join(map(str, array))
        print("What number is missing in the progression?")
        answer = prompt.string(f"Question: {array_as_string} ")
        print(array_as_string)
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is a wrong answer ;(. Correct answer was '{correct_answer}.\nLet's try again, {user_name}!')"
            )
            correct_answers = 0
    print(f"Cogratulations! {user_name}")

def main():
    welcome_user()
    ask_user()


if __name__ == "__main__":
    main()