class player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.items = []
        
        self.score = 0 
        self.max_weight = 10
    def total_weight(self):
        total = 0 
        for item in self.items:
            total = total + item.weight
        return total 
    def