def inventory(items):
    print("You have the following items:")
    for item in items:
        print("- " + item)
    

backpack = ["Water bottle", "Map", "Compass"]
inventory(backpack)
backpack.append("Swiss Army knife")
inventory(backpack)






