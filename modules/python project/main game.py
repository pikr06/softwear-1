name = input("enter your name gamer ")
age = int(input("enter your age "))
print ("welocme to the my world", name)
print("wow! you are",age, "years young")


age = int(input("Enter your age: "))

if age < 12:
    print("You are a minor. The program will now close.")
else:
    print("Welcome to the game!")
    
    
    command = ""
    while command != "lopeta":
        print("----- MAIN MENU -----")
        print("start   - Start a new game")
        print("score  - Show your score")
        print("help     - Show help")
        print("info  - Show info about the game")
        print("lopeta   - Quit the program")
        print("----------------------")
        
        command = input("Enter a command: ")
        
        if command == "start":
            print("Starting a new game... Good luck!")
        elif command == "score":
            print("Your current score is: 0")
        elif command == "help":
            print("Help: type a command from the menu and press Enter.")
        elif command == "info":
            print("This is a simple fictional game made with Python.")
        elif command == "lopeta":
            print("Thanks for playing! Goodbye.")
        else:
            print("Unknown command, please try again.")