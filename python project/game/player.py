class Player:
    def __init__ (self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.world_rooms = None
        self.items = []
        
        self.score = 0 
        self.max_weight = 10
    def total_weight(self):
        total = 0 
        for item in self.items:
            total = total + item.weight
        return total 
    def has_item(self, item_name):
        for item in self.items:
            return True
        return False
    def move(self, destination):
        self.location = destination
        print("right now you are in", self.location.name)
    def collect_item(self):
        room = self.location
        if room.item == None:
            print("There is nothing to pick up here")
        elif self.total_weight() + room.item.weight > self.max_weight:
            print("this is too heavy to carry in your bag")
        else:
            self.items.append(room.item)
            print("you have picked up", room.item.name)
            room.item = None