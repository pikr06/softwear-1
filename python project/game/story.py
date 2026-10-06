def point_system (player, points, message):
    player.score = player.score + points
    if points > 0:
        print("tick well done",message, str(points),"points" )
    else:
        print("unlucky negative tick", message, str(points),"points")

def play(player):
    player.score = 0 
    in_class = True
    print("\n new day begins,")
    print("\n--6.30am--")
    print("the alarm has rung. first class starts at 8:00 am")
    print("1) should i get up?")
    print("2) hmm lets sleep for a bit")
    print("3) lets miss the first class, I'll catch up later")
    choice = input("which one to pick?")
    if choice == "1":
        point_system(player,2,"you woke up early")
    elif choice == "2":
        point_system(player, -1, "your running late")
    elif choice =="3":
        point_system(player, -3, "you slept through the first class")
        in_class = False
    else:
        print("that wasnt an option")
        in_class = False

    if in_class == True:
        print("\n--- First Class ---")
        print("the teacher takes attendence")
        print("1) Hmm should I listen and take notes?")
        print("2) should I just text and scroll on Tiktok")
        print("3) skip class")
        choice = input("what should I do?")
        if choice == "1":
            point_system(player, 2, "your up to date with the lesson")
            if player.has_item("Notebook"):
                point_system(player, 2,"the notebook has helped with taking notes")
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
        choice = input("what should I do?")
        if choice == "1":
            point_system(player, 1, "tony shared his notes")
        elif choice == "2":
            point_system(player, -2, "starting to fall behind in class")
        else:
            print("invalid choice")
    print("\n -- 11:00pm -- (Lunch time)")
    print("1) eat with tony and friends")
    print("2) eat quick in the cafe and go study")
    print("3) eat out and go play games")
    choice = input("what should I chose")
