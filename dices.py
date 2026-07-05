
import random

print()
print("Double dice roller")
print()

while True:
    while True:
        a = input("Do you want to roll dice? (y/n): ")
        if a.lower() == "y" or a.lower() == "n":
            break
        else:
            print()
            print("Please enter a valid input.")

    if a.lower() == "y":
        n = random.randint(1, 6)
        m = random.randint(1, 6)
        print(f"The result is: ({n}, {m}).")
        print()
    else:
        print()
        print("Thanks for playing.")
        break

print()
