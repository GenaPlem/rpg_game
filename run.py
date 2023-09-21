import os
import shutil


class Player:
    """
    Class for player
    """
    def __init__(self, username):
        self.username = username
        self.attack_dmg = 10
        self.hp = 20
        self.max_hp = 50
        self.coins = 0
        self.potions = 0
        self.location = 'Cave'
        self.inventory = []


class Enemy:
    """
    Class for enemy
    """
    def __init__(self, name):
        self.name = name
        self.attack_dmg = 5
        self.max_hp = 50
        self.hp = self.max_hp


def clear():
    """
    Function to clear the terminal
    """
    os.system('clear')


def ascii_art_logo():
    """
    Function to print ascii art logo
    """
    print('''
  _____                              _       ______
 |  __ \                            ( )     |  ____|
 | |  | |_ __ __ _  __ _  ___  _ __ |/ ___  | |__  _   _  ___
 | |  | | '__/ _` |/ _` |/ _ \| '_ \  / __| |  __|| | | |/ _ \\
 | |__| | | | (_| | (_| | (_) | | | | \__ \ | |___| |_| |  __/
 |_____/|_|  \__,_|\__, |\___/|_| |_| |___/ |______\__, |\___|
                    __/ |                           __/ |
                   |___/                           |___/
    ''')


def text_align_center(text):
    """
    Function to centralize text
    """
    print(text.center(shutil.get_terminal_size()[0]))


def initialize_game():
    """
    Function to initialize the game after creating a new player
    """
    clear()
    ascii_art_logo()
    username = input('Enter your Name! ')
    player = Player(username)
    return player
    # print(f" Hey, {new_user.username}. You finally awake! Hope you're fine.")


def start_new_game(player):
    """
    Function for game intoduction
    """
    print('You wake up in a dimly lit cave, the flickering light of a campfire casting shadows on the walls.')
    print('A Stranger sits across from you, tending to the fire.\n')
    print(f'''Stranger:
        Hey {player.username}, you're finally awake.
        I heard a dragon's roar and then found you unconscious at the foot of the mountain.
        You must have been at the summit where, according to legends, a fearsome Dragon resides.
    ''')
    print(f'Your health is {player.hp}/{player.max_hp}HP')
    print('and the stranger offers you a mysterious potion.\n')
    print(f'''Stranger:
        This will help you recover
        *He takes you a mysterious potion*
        Will you drink it? (Type Y (yes) or N (no))
    ''')
    drink_potion = input('# ').lower()
    if drink_potion == 'y':
        player.hp = player.max_hp
        print(f'Your health now is {player.hp}/{player.max_hp}HP\n')
        print('''Stranger:
        Good. Now you are ready to go.
        One more thing. If you want to get more potions like this, just find the merchant in the village
        ''')
    elif drink_potion == 'n':
        print('''Stranger:
        As you say so...
        By the way, if you are interested in survive, you have to find the merchant in the village
        ''')


def show_rules():
    """
    Function to show rules of the game
    """
    clear()
    ascii_art_logo()
    print("------------------------------------------------")
    print("1. You will be presented with a list of options at each stage of the game.")
    print("2. To make a choice, simply enter the number corresponding to the option you'd like to choose.")
    print("3. To go to main menu and save the game at any time, enter '0'.")
    print("------------------------------------------------")
    text_align_center("Press 'Enter' to return to the main menu.")
    input('> ')
    main_menu()


def main_menu():
    """
    Function to show main menu
    """
    clear()
    ascii_art_logo()
    text_align_center("1. New Game")
    text_align_center("2. Load Game")
    text_align_center("3. Rules")
    text_align_center("4. Quit")

    choise = input('# ')

    if choise == '1':
        player = initialize_game()
        start_new_game(player)
    elif choise == '2':
        pass
    elif choise == '3':
        show_rules()
    elif choise == '4':
        print("Bye, hope you will come again!!")
        quit()
    else:
        print('No such options! Please select number from menu options. Press "Enter" to continue')
        input('> ')
        main_menu()


main_menu()
