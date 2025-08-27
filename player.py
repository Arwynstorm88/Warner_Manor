from constants import menu
class Player:
    def __init__(self, current_room):
        self.location = current_room
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

    def describe(self, rooms):
        if "Item" in rooms[self.location]:
            print(f'You are in the {self.location}.\nInventory: {self.inventory}\n'
                f'You see the {rooms[self.location]["Item"]}\n' + '-' * (len(menu)), '\nEnter your move:')
        else:
            print(f'You are in the {self.location}.\nInventory: {self.inventory}\n'
                f'No items to be seen here\n' + '-' * (len(menu)), '\nEnter your move:')