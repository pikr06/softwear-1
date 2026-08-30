#1
print("what is the length of the zander")
zander = int(input())
if zander >= 42:
    print("if has fulfilled the size limit well done")
else:
    print("try again")

#2
print("hello customer what is the cabin level that you have purchased ")
ticket_type = input()
if ticket_type == "lux":
    print("upper-deck cabin with a balcony.")
elif ticket_type == "a"or"A":
    print("above the car deck, equipped with a window.")
elif ticket_type == "b"or"B":
    print("windowless cabin above the car deck.")
elif ticket_type == "c" or"C":
    print(" windowless cabin below the car deck.")
else:
    print("invalid cabin class")

#3
gender = input("are you a male or a female")
if gender == "male":
    hlevels =int(input("please state your hemoglobin levels"))
    if hlevels >= 134 and hlevels <= 167:
            print("you are healthy")
    else:
          print("you are unhealthy")
if gender == "female":
      hlevels = int(input("please state your hemoglobin levels"))
      if hlevels >= 117 and hlevels <= 155:
            print("you are healthy")
      else:
            print("you are unhealthy")\

year = int(input("Enter a year: "))

#4
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
            
