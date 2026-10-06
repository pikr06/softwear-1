from game.item import Item

def menu():
    print("\n--Main Menu--")
    print("start")
    print("look")
    print("move")
    print("collect- collect the item")
    print("add - add your item")
    print("inventory - show your items")
    print("score")
    print("help")
    print("lopeta")

def look(player):
    room = player.location
    print("\n you are in", room.name)
    print(room.description)
    if room.item == None:
        print("there is no item to collect here")
    else:
        print("wow there is", room.item.name, "it weighs around", str(room.item.weight),"kg")

def show_score(player):
    print("you score at the moment is", player.score)

def move_player(player, rooms):
    print("where to?")
    options = []
    number = 1 
    for room in rooms:
        print(str(number) + ")", room.name)
        options.append(str(number))
        number = number + 1
        choice = input("number: ")
    if choice in options:
        player.move(rooms[int(choice) - 1])
    else:
        print("this does not exist")

def add_item(player):
    name = input("what item do you want to add")
    player.item.append(Item(name,0.5))
    print(name, "has been added")

def show_inventory(player):
    if len(player.items) == 0:
        print("your inventory is empty")
    else:
        print("your inventory:")
        for item in player.items:
            print(item.name,str(item.weight),"kg")
        print("weight:", player.total_weight(), player.max_weight)