"""
A game for guessing a secret three-digt number based on clues.

'Pico' when your guess has a correct digit in wrong place

'Fermi' when your guess has a correct digit in correct place

'Bagels' when your guess has a no correct digit

You have 10 tries to guess the secret number
"""

import random

MIN_NUM = 100
MAX_NUM = 999
MAX_TRIES = 10

DETAILS = """
    ===============================================================================   
    I am thining of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say :          That means:
    PICO                  One digit is correct but in the wrong position
    FERMI                 At least One digit is correct and in the right position
    BAGELS                None of the digits is correct
    ===============================================================================
    """


def get_random_number():
    """
    Return a random number ranging from 100 to 999
    """
    return random.randint(MIN_NUM, MAX_NUM)


def validate_input():
    """
    Check if the user input is an integer in the range 100 - 999. Raise ValueError if input not an integer.
    """

    attempts = 0  # Track the number of attempts

    while attempts < 3:  # Allow 3 attempts before raising ValueError
        try:
            user_input = int(input("Guess the Secret Number: > "))
            if not 100 <= user_input <= 999:
                print("\n⚠️⚠️ Invalid input. ⚠️⚠️")
                attempts += 1  # Increment the attempts count
            else:
                return user_input
        except ValueError:
            print("\n⚠️⚠️ Invalid input. ⚠️⚠️")
            attempts += 1  # Increment the attempts count

    raise ValueError("Invalid input. Exceeded maximum number of attempts.")


def check_guess(secret_number, user_guess):
    """Change input and secret number to string and compare. Print "PICO", "FERMI", and "BAGELS" accordingly."""

    user_guess_string = str(user_guess)
    secret_number_string = str(secret_number)

    if user_guess_string != secret_number_string:
        if (
            user_guess_string[0] == secret_number_string[0]
            or user_guess_string[1] == secret_number_string[1]
            or user_guess_string[2] == secret_number_string[2]
        ):
            return "FERMI   👌"
        elif (
            user_guess_string[0] == secret_number_string[1]
            or user_guess_string[0] == secret_number_string[2]
            or user_guess_string[1] == secret_number_string[0]
            or user_guess_string[1] == secret_number_string[2]
            or user_guess_string[2] == secret_number_string[0]
            or user_guess_string[2] == secret_number_string[1]
        ):
            return "PICO   🤞"
        else:
            return "BAGELS   😖"
    else:
        return "Correct"


def play_bagels():
    """
    Ask user to input a 3-digit number and check if it matches the secret random number
    """

    print(DETAILS)

    secret_number = get_random_number()

    tries = 0

    while tries < MAX_TRIES:
        user_input = validate_input()

        result = check_guess(secret_number, user_input)
        print(result)

        if result == "Correct":
            print(f"{result} !!!")
            break

        tries += 1

    if tries >= MAX_TRIES:
        print("Out of Tries")

    print(f"Took you {tries} Guesses")

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower().startswith("y"):
        print()
        play_bagels()


if __name__ == "__main__":
    # bagel()
    # validate_input()
    play_bagels()
