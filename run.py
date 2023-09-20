class Player:
    def __init__(self, username):
        self.username = username
        self.attack_dmg = 10
        self.hp = 20
        self.max_hp = 50
        self.coins = 0
        self.potions = 0
        self.inventory = []


class Enemy:
    def __init__(self, name):
        self.name = name
        self.attack_dmg = 5
        self.max_hp = 50
        self.hp = self.max_hp


def initialize_game():
    username = input('Enter your Name! ')
    new_user = Player(username)
    print(f" Hey, {new_user.username}. You finally awake! Hope you're fine.")


def show_rules():
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
    print("------------------------------------------------")
    print("1. You will be presented with a list of options at each stage of the game.")
    print("2. To make a choice, simply enter the number corresponding to the option you'd like to choose.")
    print("3. To access the main menu at any time, enter '0' or 'P'.")
    print("------------------------------------------------")
    print("Press 'Enter' to return to the main menu.")
    input('> ')
    main_menu()


def main_menu():
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
    print("1. New Game")
    print("2. Load Game")
    print("3. Rules")
    print("4. Quit")

    choise = input('# ')

    if choise == '1':
        initialize_game()
    elif choise == '2':
        pass
    elif choise == '3':
        show_rules()
    elif choise == '4':
        quit()
    else:
        print('No such options! Please select number from menu options')
        main_menu()


main_menu()
