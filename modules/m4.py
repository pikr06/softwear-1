#1
#print("what is the length of the zander")
#zander = int(input())
#if zander >= 42:
#    print("if has fulfilled the size limit well done")
#else:
#    print("try again")

#2
print("hello customer what is the cabin level that you have purchased ")
ticket_type = input()
if ticket_type == "lux":
    print("upper-deck cabin with a balcony.")
elif ticket_type == "A"or"a":
    print("above the car deck, equipped with a window.")
elif ticket_type == "B"or"b":
    print("windowless cabin above the car deck.")
elif ticket_type == "c"or"C":
    print(" windowless cabin below the car deck.")
else:
    print("you have not yet booked yet a cabin sir/madam")
