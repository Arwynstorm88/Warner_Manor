from time import sleep
from player import Player

# set total clues and empty inventory.
# set menu text for easier recall
menu = 'Move Commands: Go North | Go South | Go East | Go West | Exit'
alt_commands = 'Add to Inventory: Get "item name".\nTo see this again: Help'
total_clues = 7
inventory = []
game_running = True  # start exit condition variable

# define all functions that will be called in the loop
def type_out(text, delay=0.03):  # function to create a typing effect for end messages
    for ch in text:
        print(ch, end="", flush=True)
        sleep(delay)
    print()

def show_instructions():  #function to print a welcome message and a list of commands
    print(f'Murder at Warner Manor\nCollect all 7 clues to arrest the true murderer in the Master Bedroom'
          f'\n{menu}\n{alt_commands}\n' + '*' * (len(menu)))

def show_status(player_location, rooms):  # display location, inventory, and items seen to player
    if "Item" in rooms[player_location]:
        print(f'You are in the {player_location}.\nInventory: {inventory}\n'
              f'You see the {rooms[player_location]["Item"]}\n' + '-' * (len(menu)), '\nEnter your move:')
    else:
        print(f'You are in the {player_location}.\nInventory: {inventory}\n'
              f'No items to be seen here\n' + '-' * (len(menu)), '\nEnter your move:')

def get(location, item, clue, rooms):  # A get function to obtain item from room
    if "Item" in rooms[location]: #validate that the item is in the room
        if item != rooms[location]["Item"].lower(): #validate that the correct item is being retrived
            print(f'Sorry, you cannot get {item} from here. Please try again.\n' + '-' * (len(menu)))
            return clue
        else: #if the item is in the room and valid, add to inventory, update clue count, and delete from the dictionary
            print(f'You obtain {item}\n' + '-' * (len(menu)))
            inventory.append(item.title())
            del rooms[location]["Item"]
            clue += 1
            return clue
    else: #if no items exist let the player know their input is invalid
        print(f'There is no {item} here\n' + '-' * (len(menu)))
        return clue

def end(ending):  # function to display different endings
    global game_running
    if ending == 'quit':
        type_out('You left without identifying the murderer.\nBetter luck next time!')
    elif ending == total_clues: #If all clues are in player inventory
        type_out('Great work, Detective.\nYou have arrested the true culprit: Sam.'
                 '\nSam murdered her friend while searching the mansion for the rumored treasure of-\n'
                 'Sir Arthur Warner. In the end, the treasure was a lie to cover the crime.\nSam is sentenced to life in prison.'
                 '\nCongratulations! Thanks for playing!')
    elif ending > total_clues // 2: #if more than half of the clues are in player inventory
        type_out(
            'Not quite, Detective.\nWith the clues your collected, you accuse Alex.\nAt trial, Alex is found innocent'
            ' when missing evidence comes to light.'
            '\nYou lose your license as a detective.\nGame Over!')
    elif ending > 1: #if 2 or more clues in player inventory
        type_out('Unfortunately, the real killer planted your DNA and fingerprints on several pieces of evidence.'
                 '\nYou have been arrested and charged with murder!\nGame Over!')
    else: #if 0 or 1 clues in player inventory
        type_out(
            'As you were searching for clues, the murderer ambushes you.\nYou become the second victim of Warner Manor'
            '\nYou Lose!')
    game_running = False

def main():  # initialize game loop
    #dictionary of rooms, their valid directions, and items contained
    rooms = {
        'Foyer': {'East': 'Great Hall', 'North': 'Carport'},
        'Carport': {'East': 'Guest House', 'South': 'Foyer', 'Item': 'Bloody Tire Iron'},
        'Great Hall': {'North': 'Guest House', 'South': 'Kitchen', 'West': 'Foyer', 'East': 'Master Bedroom',
                       'Item': 'Polaroid'},
        'Guest House': {'South': 'Great Hall', 'West': 'Carport', 'East': 'Boat House', 'Item': 'Wallet'},
        'Boat House': {'West': 'Guest House', 'Item': 'Half Smoked Cigarette'},
        'Kitchen': {'North': 'Great Hall', 'West': 'Library', 'East': 'Bathroom', 'Item': "Guest List"},
        'Library': {'East': 'Kitchen', 'Item': 'Confession Letter'},
        'Bathroom': {'West': 'Kitchen', 'North': 'Master Bedroom', 'Item': 'Bloody Sweater'},
        'Master Bedroom': {'West': 'Great Hall', 'South': 'Bathroom', 'Item': 'Body'}
    }
    player = Player('Foyer')
    clues_collected = 0

    show_instructions()  # Show introduction, goal, and commands to player

    while game_running:  # Create Exit Condition
        show_status(player.location, rooms)  # display status from function
        command = input('>').lower().strip()  # Get user input on command, make lower case, and strip unneeded spaces
        split_command = command.split()  # split the command into a list of single words
        if command in ('exit', 'quit'):  # Exit the game
            end('quit')
        elif command == 'help':  # reprint directions for user to remember commands
            show_instructions()
        elif len(split_command) == 2 and split_command[0] == 'go':  # validate go command and call move function
            player.move(split_command[1], rooms)
            if player.location == 'Master Bedroom':
                end(clues_collected)
        elif len(split_command) >= 2 and split_command[0] == 'get':  # validate get command and call get function
            item_to_get = " ".join(split_command[1:])
            clues_collected = get(player.location, item_to_get, clues_collected, rooms)
        else:  # if the input is invalid let the user know
            print('Invalid command. Please try again\n' + '-' * (len(menu)))

if __name__ == '__main__': main()