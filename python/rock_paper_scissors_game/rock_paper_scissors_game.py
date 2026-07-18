
import random

list_of_choices = ("🪨",  "📃", "✂️")
dictionary_of_choices = {"r": "🪨", "p": "📃", "s": "✂️"}

program_has_run = False
want_to_continue = "y"


def play_game(list_of_choices, dictionary_of_choices, program_has_run, want_to_continue):
    while True:
        if program_has_run == True:
            print()
            want_to_continue = (
                input("Do you want to continue? (y/n): ")).lower()

        if want_to_continue == "y":
            while True:
                print()
                random_value = random.randint(0, 2)
                user_input = (
                    input("Rock, paper or scissors? (r/p/s): ")).lower()
                computer_choice = list_of_choices[random_value]

                def choices(user_input, computer_choice):
                    try:
                        print(
                            f"You chose: {dictionary_of_choices[user_input]}")
                    except IndexError or TypeError or ValueError or KeyError:
                        return "ERROR"

                    print(f"Computer chose: {computer_choice}")

                if user_input == "r":
                    choices(user_input, computer_choice)
                    if random_value == 0:
                        print("Draw!")
                    elif random_value == 1:
                        print("You Lose!")
                    elif random_value == 2:
                        print("You Win!")
                    break
                elif user_input == "p":
                    choices(user_input, computer_choice)
                    if random_value == 0:
                        print("You Win!")
                    elif random_value == 1:
                        print("Draw!")
                    elif random_value == 2:
                        print("You Lose!")
                    break
                elif user_input == "s":
                    choices(user_input, computer_choice)
                    if random_value == 0:
                        print("You Lose!")
                    elif random_value == 1:
                        print("You Win!")
                    elif random_value == 2:
                        print("Draw!")
                    break
                else:
                    print("Invalid Choice! ")

        elif want_to_continue == "n":
            print("Thanks for playing.")
            print()
            break
        else:
            print("Invalid Input! ")

        program_has_run = True


play_game(list_of_choices, dictionary_of_choices,
          program_has_run, want_to_continue)
