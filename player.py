
class Player:
    def __init__(self, starting_room):
        self.location = starting_room
        self.inventory = []

    def move(self, direction, rooms):
        VALID_MOVES = {'North', 'South', 'East', 'West'}
        movement = direction.capitalize()
        if movement not in VALID_MOVES:
            print('Invalid command. Please try again.\n' + '-' * 20)
            return self.location
        elif movement in rooms[self.location]:
            new_location = rooms[self.location][movement]
            print(f'You moved to the {new_location}\n' + '-' * 20)
            self.location = new_location
            return self.location
        else:
            print(f'Sorry, you cannot move {direction} from here. Please try again.\n' + '-' * 20)
            return self.location