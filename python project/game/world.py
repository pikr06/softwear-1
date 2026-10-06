from game.item import Item
from game.room import Room

def create_rooms():


    dorm = Room("Dorm room", "Your own personal room.", Item("Pencil", 1))
    campus = Room("Campus ", "The busy middle of campus.", None)
    lecture = Room("Lecture hall", "Rows of seats and a big whiteboard.", Item("textbook", 3))
    cafeteria = Room("Cafeteria", "It smells tasty! .", Item("sandwich",2))
    library = Room("Library", "shush others are studying", Item("laptop", 4))
    gym = Room("Gym", "Trying to get fit?.", Item("gym_bag", 3))

    return [dorm, campus, lecture, cafeteria, library, gym]