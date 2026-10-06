import os

from game.player import Player
from game.world import create_rooms
from game import menu
from game import story

file = open("intro.txt", "r")
print(file.read())
file.close()

name = input("Enter your name: ")
rooms = create_rooms()
player = None

if os.path.exists(saving.save_filename(name)):
    answer = input("A saved game was found. Continue it? (yes/no): ")
    if answer == "yes":
        player = saving.load_game(name, rooms)
        print("Welcome back,", player.name + "! Your score is", player.score)

if player is None:
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
    menu.show_menu()
    command = input("\nEnter a command: ")

    if command == "start":
        story.play_day(player)
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
    elif command == "save":
        saving.save_game(player, rooms)
    elif command == "lopeta":
        saving.save_game(player, rooms)
        print("Thanks for playing,", player.name)
    else:
        print("Invalid command.")