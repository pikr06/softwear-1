from game.item import Item
from game.room import Room

def create_rooms():
    notebook = Item("Notebook", 1)
    textbook = Item("Textbook", 4)
    coffee = Item("Coffee", 0.5)
    laptop = Item("Laptop", 3)
    gym_bag = Item("Gym bag", 3)

    dorm = Room("Dorm room", "Your small but cosy room.", notebook)
    yard = Room("Campus yard", "The busy middle of campus.", None)
    lecture = Room("Lecture hall", "Rows of seats and a big whiteboard.", textbook)
    cafeteria = Room("Cafeteria", "It smells like coffee and fries.", coffee)
    library = Room("Library", "Quiet. Very quiet.", laptop)
    gym = Room("Gym", "Weights clanging in the background.", gym_bag)

    return [dorm, yard, lecture, cafeteria, library, gym]