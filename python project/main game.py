name = input("enter your name gamer ")
age = int(input("enter your age "))
print ("welocme to the my world", name)
print("wow! you are",age, "years young")
if age < 12:
      print("oh no you are too young to play")
else:
    print("start the game")
    
    commands = ""
    difficulty = input("what is the difficulty")
while commands != "lopetia":
    commands = input("enter your commands:" )
    if commands == "start":
        print("starting a new game ----- welcome to world")
    elif commands == "score":
        print("your socre right now is 0")
    elif commands == "help":
        print("state your needs")
    elif commands == "continue":
        print("opening saved data")
    elif commands == "options":
        print("difficulty")

        difficulty = input("what is the difficulty")
    if difficulty == "easy":
        print("you have selected easy mode")
    elif difficulty == "normal":
        print("you have selected normal mode")
    elif difficulty == "hard":
        print("this is the hardest mode are you sure?:")
        accept = input ()
        if accept == "yes":
            print("be warned")
        if accept == "no":
            print("that is dine")
            
else:
    print ("invalid command")



    





