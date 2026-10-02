with open("shopping.txt", "a") as file:
    file.write("peaches,apples,gams\n")

with open("shopping.txt", "w") as file:
    file.write("peaches\napples\ngams\n")

with open("shopping.txt", "r") as file:
    data = file.read()

print(data)

with open("shopping.txt", "w") as file:
    file.write("peaches\napples\ngams\n")

with open("shopping.txt", "r") as file:
    items = file.read().splitlines()  

print(items)
print("Number of items:", len(items))
