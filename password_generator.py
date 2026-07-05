# The password consists of random (letters, numbers and symbols). Space is not allowed.
# Randomly generate number of (total characters, letters, numbers and symbols).
# Randomly decide 8 to 13 characters.
# Randomly decide positions of every character.
# Assemble the password and print it out.

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation


def generate(given_choices):
    try:
        print()
        print()
        num_of_characters = int(input(
            "Enter password length 8-50 (Enter invalid input for random decision 8-13): "))
        print()
        print(f"Password length (User chosen): {num_of_characters}")
    except:
        num_of_characters = 0

    if num_of_characters < 8 or num_of_characters > 50 or num_of_characters == 0:
        num_of_characters = random.randint(8, 13)
        print()
        print(f"Password length (Randomly chosen): {num_of_characters}")

    print("Password: "+"".join(random.choices(characters, k=num_of_characters)))
    print()


generate(characters)
