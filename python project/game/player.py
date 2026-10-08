from game.item import Item


class Player:
    def __init__ (self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.world_rooms = None
        self.items = []
        self.score = 0 
        self.max_weight = 5

    def total_weight(self):
        total = 0 
        for item in self.items:
            total = total + item.weight
        return total 
    
    def has_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return True
        return False
    
    def move(self, room):
        self.location = room
        print(self.location.name)

    def collect_item(self):
        room = self.location
        if room.item is None:
            print("There is nothing to pick up here")
        else:
            item = room.item
            if self.total_weight() + item.weight > self.max_weight:
                print("The", item.name, "is too heavy. You can't carry any more.")
                choice = input("do you wanna drop soemthing ?")
                
                if choice == "yes":
                    self.drop_item(False)
                    if self.total_weight() + item.weight <= self.max_weight:
                       self.items.append(item)
                       self.score += item.points
                       print("you have picked up", item.name)
                       print("tick you picked up", item.points)
                       room.item = None
                    else:
                        print("you still dont have enough space")
                else:
                        print("you have decided not to pick it up ")
            else:
                self.items.append(item)
                self.score += item.points
                print("you have picked up", item.name)
                print("tick you picked up", item.points, "points")
                room.item = None

    def drop_item(self, in_room = True):
            if len(self.items) == 0:
                print("You have no items to drop.")
                return
            
            print("\nWhich item do you want to drop?")
            options = []
            number = 1

            for item in self.items:
                print(str(number) + ")", item.name, "(", item.weight, "kg )")
                options.append(str(number))
                number += 1

            choice = input("number:")

            if choice in options:
                dropped = self.items.pop(int(choice)-1)
                print("you dropped", dropped.name)

                if in_room:
                    if self.location.item is None:
                        self.location.item = dropped
                    else:
                        print("the room already has an item")
                    return dropped
                        
            else:
                print("the room aleady has an item:")
                return None 