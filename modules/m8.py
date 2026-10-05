#first, second, third, fourth = ["spring", "summer" , "autumn", "winter"]
#month = int(input("enter a number" ))
#while month >= 1 or month <= 12: 
#    month = int(input("enter a number" ))
#    if 1 <= month <= 3:
#        print ("your szn is winter")
#    elif 4 <= month <= 6:
#        print ("your szn is spring")
#    elif 7<= month <= 9:
#        print("your szn is summer")
#    elif 10<= month <= 12:
#        print ("your szn is autumn")
#    else:
#p
# break


names = set()
while True:
    n = input("name")
    if n == "":
        break 
    if n in names:
        print("already exists")
    else:
        print("new name ")
        names.add(n)
for n in names:
    print(n)

airports = {}
while True:
    print("enter a airport")
    print("airport info")
    print("exit")
    choice = ("enter a choice")
    if choice == "1":
        ICAO = input("Enter the Icao number")
        name = input("Enter the airport name")
        
        airports[ICAO] = name
        print("the airport has been added")
    elif choice == "2":
        ICAO = input("Enter the Icao number")
        if ICAO in airports:
            print(airports[ICAO]) 
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Invalid option.")