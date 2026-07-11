# List all the options and let the user choose
# If the user choses view order, display their item and price sum of money
# Repeat the loop until the checkout or cancelation of order
# Cancel the order if user selects cancel
# Checkout if user selects checkout option
# Checkout cannot be done with an empty item
# Only allow the user to exit if the cart is empty


import sys


cart = []
item_dict = {1: "Espresso: $2.5", 2: "Latte: $3.5",
             3: "Cappuccino: $3.0", 4: "Americano: $2.0"}
price_dict = {1: 2.5, 2: 3.5,
              3: 3.0, 4: 2.0}


def menu():
    choice = int(input("\nCoffee Menu:\n"
                       "1. Espresso: $2.5\n"
                       "2. Latte: $3.5\n"
                       "3. Cappuccino: $3.0\n"
                       "4. Americano: $2.0\n"
                       "5. View Order\n"
                       "6. Checkout\n"
                       "7. Cancel\n"
                       "8. Exit\n"
                       "Choose an option (eg. 3 or 4 etc): ").strip())
    return choice


def view_order(cart, item_dict, price_dict):
    if cart != []:
        print()
        print("Your Order:")
        for key in cart:
            print(f"* {item_dict[key]}")
        total = sum(price_dict[k] for k in cart)
        print(f"Your Total: ${total}")
        print()

    else:
        print()
        print("You haven't ordered anything. Please order first.")


def checkout(cart):
    if cart != []:
        while True:
            want_to_checkout = input("Checkout? (y/n): ").lower().strip()
            print()

            if want_to_checkout == "y":
                print("Checkout Successful!")
                cart = []
                print()
                break

            elif want_to_checkout == "n":
                break

            else:
                print("Please choose a valid option.")
                print()

    return cart


def cancel_order(cart):
    if cart != []:
        while True:
            print()
            want_to_cancel = input(
                "Cancel your order? (y/n): ").lower().strip()

            if want_to_cancel == "y":
                print()
                print("Your order has been canceled.")
                cart = []
                break

            elif want_to_cancel == "n":
                print()
                print("Your order has not been canceled.")
                break

            else:
                print()
                print("Please choose a valid option.")

    else:
        print()
        print("You haven't ordered anything. Please order first.")

    return cart


def exit_cafe(cart):
    if cart != []:
        print()
        print("Please cancel your order first.")

    else:
        while True:
            print()
            want_to_exit = input("Exit? (y/n): ").lower().strip()

            if want_to_exit == "y":
                print()
                print("Thank You! Please visit us again.")
                print()
                sys.exit()

            elif want_to_exit == "n":
                break

            else:
                print()
                print("Please choose a valid option.")


while True:
    try:

        choice = menu()

        if choice >= 1 and choice <= 4:
            cart.append(choice)
            print()
            print(f"You added {item_dict[choice]} to your order.")

        elif choice >= 5 and choice <= 8:

            if choice == 5:
                view_order(cart, item_dict, price_dict)

            elif choice == 6:
                view_order(cart, item_dict, price_dict)
                cart = checkout(cart)

            elif choice == 7:
                cart = cancel_order(cart)

            elif choice == 8:
                exit_cafe(cart)

        else:
            print()
            print("Please choose a valid option from 1 to 8.")

    except ValueError:
        print()
        print("Please choose a valid option.")
