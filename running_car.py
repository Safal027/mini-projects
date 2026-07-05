# Ask the user for input
# If user enters help display all command with their functions
# If user enters any other command, act accordingly
# Keep asking user for input until command of stop
# Terminate after stop command

def initalizing():
    print()
    print("Welcome to the car racing game! ")
    print()
    print("Enter 'help' to display the help menu. ")
    print()


def play_game(car_started):
    while True:
        command = (input("> ")).lower()

        if command == "help":
            print("start: to start the car "
                  "\nstop: to stop the car "
                  "\nquit: to terminate the game "
                  "\nhelp: to display the help menu ")
            print()
        elif command == "start" and car_started == False:
            print("Car started...Ready to go! ")
            print()
            car_started = True
        elif command == "stop" and car_started == True:
            print("Car stopped! ")
            print()
            car_started = False
        elif command == "start" and car_started == True:
            print("You have already started the car. ")
            print()
        elif command == "stop" and car_started == False:
            print("Please start the car first. ")
            print()
        elif command == "quit":
            print("Thank you for playing! ")
            print()
            break
        else:
            print("I don't understand that... ")
            print()


initalizing()

play_game(False)
