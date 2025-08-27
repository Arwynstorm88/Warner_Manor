from time import sleep
from player import Player
from room import *
from constants import *

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

    player = Player('Foyer')

    show_instructions()  # Show introduction, goal, and commands to player

    while game_running:  # Create Exit Condition
        player.describe(room_map)  # display status from function
        command = input('>').lower().strip()  # Get user input on command, make lower case, and strip unneeded spaces
        split_command = command.split()  # split the command into a list of single words
        if command in ('exit', 'quit'):  # Exit the game
            end('quit')
        elif command == 'help':  # reprint directions for user to remember commands
            show_instructions()
        elif len(split_command) == 2 and split_command[0] == 'go':  # validate go command and call move function
            direction_raw = split_command[1]
            direction = direction_raw.title()
            if direction not in VALID_MOVES:
                print('Invalid command. Please try again\n' + '-' * len(menu))
            else:
                success = player.move(direction, room_map)
                if success:
                    print(f'You moved to the {player.location}\n' + '-' * len(menu))
                    if player.location == 'Master Bedroom':
                        end(player.clue_count)
                else:
                    print(f'Sorry, you cannot move {direction.lower()} from here. Please try again.\n' + '-' * len(menu))
        elif len(split_command) >= 2 and split_command[0] == 'get':  # validate get command and call get function
            item_to_get = " ".join(split_command[1:])
            item = item_to_get.title()
            room = room_map[player.location]
            room_item = room.get("Item")
            if room_item:
                success = player.get(item, room_map)
                if success:
                    print(f'You found {item} at {player.location}\n' + '-' * len(menu))
                else:
                    print(f'Sorry you can not get {item} from here. Please try again.\n' + '-' * len(menu))
            else:
                print(f'There is no {item} here\n' + '-' * len(menu))
        else:  # if the input is invalid let the user know
            print('Invalid command. Please try again\n' + '-' * len(menu))

if __name__ == '__main__': main()