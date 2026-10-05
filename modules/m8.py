first, second, third, fourth = ["spring", "summer" , "autumn", "winter"]
month = int(input("enter a number" ))
while month >= 1 or month <= 12: 
    month = int(input("enter a number" ))
    if 1 <= month <= 3:
        print ("your szn is winter")
    elif 4 <= month <= 6:
        print ("your szn is spring")
    elif 7<= month <= 9:
        print("your szn is summer")
    elif 10<= month <= 12:
        print ("your szn is autumn")

