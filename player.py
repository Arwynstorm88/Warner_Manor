
class Player:
    def __init__(self, starting_room,):
        self.location = starting_room
        self.inventory = []
        self.clue_count = 0

    def move(self, direction, rooms):
        if direction in rooms[self.location]:
            new_location = rooms[self.location][direction]
            self.location = new_location
            return True
        else:
            return False

    def get(self, item, rooms): # A get function to obtain item from room
        room_item = rooms[self.location].get("Item")
        if item == room_item:
            self.clue_count += 1
            self.inventory.append(item)
            rooms[self.location].pop("Item", None)
            return True
        return False
