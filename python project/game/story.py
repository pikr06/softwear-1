from game import menu

def point_system (player, points, message):
    player.score = player.score + points
    if points > 0:
        print("tick well done",message, str(points),"points" )
    else:
        print("unlucky negative tick", message, str(points),"points")

def ask_pickup(player):
    room = player.location
    if room.item is not None:
        print("\nYou see a", room.item.name)
        choice = input("Pick it up? (yes/no): ")
        if choice == "yes":
            player.collect_item()
        else:
            print("You leave the item where it is.")

def play(player):
    player.score = 0 
    in_class = True
    
    print("\n new day begins,")
    print("\n--7.30am--")
    print("the alarm has rung. first class starts at 8:00 am")
    print("Pick where you want to start your day.")
    print("1) should i get up?")
    print("2) hmm lets sleep for a bit")
    print("3) lets miss the first class, I'll catch up later")
    choice = input("which one to pick? ") 
    menu.move_player(player, player.world_rooms)
    menu.look(player)
    ask_pickup(player)

    if choice == "1":
        point_system(player,2,"you woke up early")
    elif choice == "2":
        point_system(player, -1, "your running late")
    elif choice =="3":
        point_system(player, -3, "you slept through the first class")
        in_class = False
    else:
        print("invalid option")
        in_class = False
    if in_class:
        print("\nGo to the Lecture hall.")
        menu.move_player(player, player.world_rooms)
        menu.look(player)
        ask_pickup(player)
    if player.location.name != "Lecture hall":
            print("You are not in the Lecture hall. You miss class.")
            point_system(player, -3, "You skipped class")
            in_class = False
    if in_class == True:
        print("\nFirst Class")
        print("the teacher takes attendence")
        print("1) Hmm should I listen and take notes?")
        print("2) should I just text and scroll on Tiktok")
        print("3) skip class")
        choice = input("what should I do? ")
        if choice == "1":
            point_system(player, 2, "your up to date with the lesson")
            if player.has_item("textbook"):
                point_system(player, 2,"the textbook has helped with taking notes")
        elif choice == "2":
            point_system(player, -1, "you wasted your time in class now you need to catch up")
        elif choice =="3":
            point_system(player, -3, "you skipped class, the teacher has now realised")
        else:
            print("inavlid choice")
    else:
        print("\n you have now missed ths first class")
        print("1) text tony for his notes")
        print("2) ignore and start procrastnaing")
        choice = input("what should I do? ")
        if choice == "1":
            point_system(player, 1, "tony shared his notes")
        elif choice == "2":
            point_system(player, -2, "starting to fall behind in class")
        else:
            print("invalid choice")
        
    print("\n  11:00am : (Lunch time)")
    menu.move_player(player, player.world_rooms)
    menu.look(player)
    ask_pickup(player)
    if player.location.name != "Cafeteria":
        print("You skipped lunch.")
        point_system(player, -1, "Skipped lunch")
    else:
        print("1) eat with tony and friends")
        print("2) eat quick in the cafe and go study")
        print("3) eat out and go play games")
        choice = input("what should I chose? ")
        if choice == "1":
            point_system(player, 1, "You spent time with friends")
        elif choice == "2":
            point_system(player, 2, "You studied")
            if player.has_item("textbook"):
                point_system(player, 1, "textbook helped")
        elif choice == "3":
            point_system(player, -1, "You wasted time")
        else:
            print("invalid choice")

    print("\n Evening time")
    print("wow I finally have free time, what should do? ")
    menu.move_player(player, player.world_rooms)
    menu.look(player)
    ask_pickup(player)
    if player.location.name == "Gym":
        point_system(player, 2, "well done you worked out")
        if player.has_item("gym_bag"):
                point_system(player, 1, "you have been staying healthy")
    elif player.location.name == "library":
        point_system(player, 3, "You studied hard")
        if player.has_item("laptop"):
            point_system(player, 1, "Laptop helped")
    elif player.location.name == "Campus ":
        point_system(player, -2, "You partied")

    print("\n===== END OF THE DAY =====")
    if player.score >= 5:
        print("Your final score is", player.score,"well done you have done well")
    else:
        print("Your final score is", player.score,"you havent done too good try again")
    print("press start to play again")
