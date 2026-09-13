#rounds = int(input("how many greeting:"))
#finished_rounds = 0
#while finished_rounds < rounds:
#    print("good mornings")
#    finished_rounds = finished_rounds 

#command = input("Enter command: ")
#while command != "stop":
#    print("Executing command: " + command)
#    command = input("Enter command: ")
#print("Execution stopped.")


#command = input("Enter command: ")
#while command != "stop":
#    if command == "MAYDAY":
#        break
#    print("Executing command: " + command)
#    command = input("Enter command: ")
#print("Execution stopped.")

import random

def roll_dice(sides):          # "sides" is a parameter
    return random.randint(1, sides)


# --- main program ---
sides = int(input("How many sides does the dice have? "))
result = 0

while result != sides:         # roll until the maximum comes up
    result = roll_dice(sides)  # "sides" here is the argument
    print(f"Rolled {result}")

print(f"Got the maximum {sides}!")
   
