
import random

n = random.randint(1, 100)
c = 0
want_to_continue = "y"

print()

while True:
    print("Welcome!")
    while True:
        print()
        while True:
            try:
                a = int(input("Enter a number from 1 to 100: "))
                break
            except ValueError:
                print("Please enter a valid number!")
                print()
        c = c + 1

        if a < n:
            print("Too Low!")
        elif a > n:
            print("Too High!")
        elif a == n:
            print()
            print("Congratulations! You guessed the number!")
            print(f"Number of tries: {c}")
            break

    while True:
        print()
        try:
            want_to_continue = (
                input("Do you want to continue? (y/n): ")).lower()
            print()
            break
        except:
            print("Please enter a valid input!")

    print()

    if want_to_continue == "n":
        print("Thanks for playing!")
        print()
        break
