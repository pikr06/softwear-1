import os

from game.player import Player
from game.world import create_rooms
from game import menu
from game import story



name = input("Enter your name: ")
rooms = create_rooms()
age = int(input("Enter your age: "))
print("Name:", name)
print("Age:", age)
if age < 12:
        print("You are too young to play. Shutting down.")
        exit()
print("Welcome,", name + "!")
player = Player(name, age, rooms[0])

player.world_rooms = rooms

command = ""
while command != "lopeta":
    menu.menu()
    command = input("\nEnter a command: ")

    if command == "start":
        story.play(player)
        break
    elif command == "look":
        menu.look(player)
    elif command == "move":
        menu.move_player(player, rooms)
    elif command == "collect":
        player.collect_item()
    elif command == "drop":
        menu.drop_item(player)
    elif command == "add":
        menu.add_item(player)
    elif command == "inventory":
        menu.show_inventory(player)
    elif command == "score":
        menu.show_score(player)
    
    elif command == "lopeta":
        break
    else:
        print("Invalid command.")