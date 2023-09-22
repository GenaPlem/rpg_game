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
        self.explored_locations = []
        self.visited_locations = []


class Enemy:
    """
    Class for enemy
    """
    def __init__(self, name, attack_dmg, max_hp):
        self.name = name
        self.attack_dmg = attack_dmg
        self.max_hp = max_hp
        self.hp = self.max_hp


def clear():
    """
    Helper function to clear the terminal
    """
    os.system('clear')


def ascii_art_logo():
    """
    Function to print ascii art logo
    """
    clear()
    print('''
  _____                              _       ______
 |  __ \\                            ( )     |  ____|
 | |  | |_ __ __ _  __ _  ___  _ __ |/ ___  | |__  _   _  ___
 | |  | | '__/ _` |/ _` |/ _ \\| '_ \\  / __| |  __|| | | |/ _ \\
 | |__| | | | (_| | (_| | (_) | | | | \\__ \\ | |___| |_| |  __/
 |_____/|_|  \\__,_|\\__, |\\___/|_| |_| |___/ |______\\__, |\\___|
                    __/ |                           __/ |
                   |___/                           |___/
    ''')


def text_align_center(text):
    """
    Function to centralize text
    """
    print(text.center(shutil.get_terminal_size()[0]))


def continue_input():
    """
    Helper function to continue the game
    """
    input("> Press 'Enter' to continue")
    # to remove the input text above (works only for Unix-like os)
    print("\033[A                             \033[A")


def show_stats(player):
    """
    Function to show stats of player
    """
    clear()
    max_length = 30
    print('*' * max_length)

    lines = [
        f"| LOCATION: {player.location}",
        f"| {player.username}",
        f"| HP: {player.hp}/{player.max_hp}",
        f"| DMG: {player.attack_dmg}",
        f"| Potions: {player.potions}",
        f"| Coins: {player.coins}"
    ]

    for line in lines:
        padding = max_length - len(line) - 1
        print(line + ' ' * padding + '|')

    print('*' * max_length + '\n')


def battle_stats(enemy):

    enemy_stats = f'| {enemy.name} | {enemy.hp}/{enemy.max_hp}HP | {enemy.attack_dmg} ATK DMG |\n'

    max_length = len(enemy_stats) - 1
    num_symbols = max_length - len('Battle') - 2

    title = '|' + '=' * num_symbols + ' Battle ' + '=' * num_symbols + '|'

    text_align_center(title)
    text_align_center(enemy_stats)


def initialize_game():
    """
    Function to initialize the game after creating a new player
    """
    while True:
        ascii_art_logo()
        username = input('Enter your name Hero! \n')
        if 15 >= len(username.strip()) > 1:
            player = Player(username)
            return player
        else:
            print('Name should be more than 1 symbol and less then 10\n')
            continue_input()


def prolog(player):
    """
    Function for game prolog
    """
    show_stats(player)
    print('You wake up in a dimly lit cave, the flickering light of a campfire casting shadows on the walls.')
    print('A Stranger sits across from you, tending to the fire.\n')
    continue_input()
    show_stats(player)
    print(f'''Stranger:
        Hey {player.username}, you're finally awake.
        I heard a dragon's roar and then found you unconscious at the foot of the mountain.
        You must have been at the summit where, according to legends, a fearsome Dragon resides.
    ''')
    continue_input()
    show_stats(player)
    while True:
        print(f'''Stranger:
        This will help you recover
        *He offers you a mysterious potion*
        *Will you drink it? (Type Y (yes) or N (no))*
    ''')
        drink_potion = input('# ').lower()
        if drink_potion == 'y':
            player.hp = player.max_hp
            show_stats(player)
            print(f'Your health now is {player.hp}/{player.max_hp}HP\n')
            print('''Stranger:
            Good. Now you are ready to go.
            One more thing. If you want to get more potions like this, just find the merchant in the village
            ''')
            continue_input()
            break
        elif drink_potion == 'n':
            show_stats(player)
            print('''Stranger:
            As you say so...
            By the way, if you are interested in survive, you have to find the merchant in the village
            ''')
            continue_input()
            break
        else:
            show_stats(player)
            print("No such options. Your answer might be Y or N\n")
            continue_input()
            show_stats(player)


def battle(player, enemy):
    """
    Function the start the battle between player and enemy
    """
    while True:
        show_stats(player)
        battle_stats(enemy)
        print(f'1. Attack the {enemy.name}')
        print('2. Block')
        print('3. Try to run away')

        choise = input('# ')

        if choise == '1':
            enemy.hp -= player.attack_dmg
            if enemy.hp > 0:
                print(f'You hit {enemy.name} for {player.attack_dmg} damage')
                continue_input()
                print(f'{enemy.name} hits you back dealing {enemy.attack_dmg} DMG')
                player.hp -= enemy.attack_dmg
                continue_input()
                if player.hp > 0:
                    show_stats(player)
                    battle_stats(enemy)
                else:
                    return False
            else:
                show_stats(player)
                battle_stats(enemy)
                print(f'You hit {enemy.name} for {player.attack_dmg} damage')
                continue_input()
                print('Exellent. You win!')
                return True
        else:
            print('No such option.')
            continue_input()


def game_over():
    print('GAME OVER!')
    continue_input()
    print('1. Go to main menu')
    print('2. Quit the game')
    choise = input('# ')
    if choise == '1':
        main_menu()
    elif choise == '2':
        exit()


def cave_actions(player):
    """
    Function with actions for Cave location
    """
    show_stats(player)
    print('1. Leave the Cave')
    print('2. Explore the Cave')
    print('3. Talk to Stranger')

    choise = input('# ')

    if choise == '1':
        player.location = 'Forest'
        show_stats(player)
        print('You left the Cave and now you are in the Forest\n')
        continue_input()
        forest_actions(player)
    elif choise == '2':

        if 'Cave' not in player.explored_locations:
            show_stats(player)
            print('Exploring the Cave...')
            continue_input()
            print('Well well! You find someting')
            print("It's a lit bag of money!!")
            print('*You find 10 coins!*')
            continue_input()
            player.coins += 10
            player.explored_locations.append('Cave')
            show_stats(player)
            cave_actions(player)
        else:
            show_stats(player)
            print('You are already explored this location!\n')
            continue_input()
            cave_actions(player)

    elif choise == '3':
        show_stats(player)
        print('''Stranger:
        Ah, you're still here?
        Time waits for no one, especially not in these treacherous lands. I suggest you move along.
        I have my own matters to attend to.
        ''')
        continue_input()
        cave_actions(player)
    else:
        print("No such options. Choose it from the options list.\n")
        continue_input()
        cave_actions(player)


def forest_actions(player):
    """
    Function with actions in Forest location
    """
    if 'Forest' not in player.visited_locations:
        enemy_wolf = Enemy('Wolf', 5, 40)
        show_stats(player)
        print('As you step out of the cave, you feel the fresh air and sun on your face.')
        print('Suddenly, a low growl comes from the bushes. A ferocious wolf lunges at you.\n')
        continue_input()
        print('You was attacked by Wolf')
        print('*The Wolf bites you, dealing 5 damage!\n')
        continue_input()
        player.hp -= 5
        show_stats(player)
        print('You quickly draw your sword, realizing that the forest is not as welcoming as it seemed.')
        print("It's you or the Wolf now, and the fight for survival begins.\n")
        continue_input()
        if battle(player, enemy_wolf):
            continue_input()
            forest_actions(player)
        else:
            show_stats(player)
            battle_stats(enemy_wolf)
            game_over()

    else:
        show_stats(player)
        print('1. Enter the Cave')

        choise = input('# ')

        if choise == '1':
            player.location = 'Cave'
            show_stats(player)
            print('You are enter the Cave\n')
            continue_input()
            cave_actions(player)
        else:
            print("No such options. Choose it from the options list.\n")
            continue_input()
            forest_actions(player)


def show_rules():
    """
    Function to show rules of the game
    """
    ascii_art_logo()
    print("-----------------------RULES-------------------------")
    print("1. You will be presented with a list of options at each stage of the game.")
    print("2. To make a choice, simply enter the number corresponding to the option you'd like to choose.")
    # print("3. To go to main menu and save the game at any time, enter '0'.")
    print("-----------------------------------------------------")
    continue_input()
    main_menu()


def main_menu():
    """
    Function to show main menu
    """
    ascii_art_logo()
    text_align_center("1. New Game")
    text_align_center("2. Load Game")
    text_align_center("3. Rules")
    text_align_center("4. Quit")

    choise = input('# ')

    if choise == '1':
        player = initialize_game()
        prolog(player)
        cave_actions(player)
    elif choise == '2':
        pass
    elif choise == '3':
        show_rules()
    elif choise == '4':
        print("Bye, hope you will come again!!")
        quit()
    else:
        print('No such options! Please select number from menu options. Press "Enter" to continue\n')
        continue_input()
        main_menu()


main_menu()
