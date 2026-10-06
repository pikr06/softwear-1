name = input("enter your name gamer ")
age = int(input("enter your age "))
print ("welocme to the my world", name)
print("wow! you are",age, "years young")
if age < 12:
      print("oh no you are too young to play")
else:
    print("start the game")
    
commands = input("enter a command")
#difficulty = input("what is the difficulty")
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
    #elif commands == "options":
     #   print("difficulty")

    #    difficulty = input("what is the difficulty")
    #if difficulty == "easy":
    #    print("you have selected easy mode")
    #elif difficulty == "normal":
    #    print("you have selected normal mode")
    #elif difficulty == "hard":
    #    print("this is the hardest mode are you sure?:")
    #    accept = input ()
    #    if accept == "yes":
    #        print("be warned")
    #    if accept == "no":
    #        print("that is dine")
            
#else:
#    print ("invalid command")

inventory = []
score = 0
def start_game():
    print("starting a new game ----- welcome to world")


def show_score():
    print("your score right now is", score)


def show_help():
    print("state your needs")


def continue_game():
    print("opening saved data")


def show_options():
    print("difficulty")

def add_item():
    item = input("what item do you want to add to your inventory? ")
    inventory.append(item)
    print(item, "was added to your inventory")

def show_inventory():
    if len(inventory) == 0:
        print("your inventory is empty")
    else:
        print("your inventory:")
        for thing in inventory:
            print("-", thing)



    





