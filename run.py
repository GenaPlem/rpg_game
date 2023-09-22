import os
import shutil
import random


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
        self.potions = 1
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
    ascii_art = [
        '          ',
        ' _____                              _       ______           ',
        ' |  __ \\                            ( )     |  ____|           ',
        ' | |  | |_ __ __ _  __ _  ___  _ __ |/ ___  | |__  _   _  ___ ',
        ' | |  | | \'__/ _` |/ _` |/ _ \\| \'_ \\  / __| |  __|| | | |/ _ \\',
        ' | |__| | | | (_| | (_| | (_) | | | | \\__ \\ | |___| |_| |  __/',
        ' |_____/|_|  \\__,_|\\__, |\\___/|_| |_| |___/ |______\\__, |\\___|',
        '                    __/ |                           __/ |      ',
        '                   |___/                           |___/       ',
        '          '
    ]
    terminal_width, _ = shutil.get_terminal_size()

    for line in ascii_art:
        padding = (terminal_width - len(line)) // 2
        print(' ' * padding + line)


def text_align_center(text):
    """
    Helper function to centralize text
    """
    print(text.center(shutil.get_terminal_size()[0]))


def continue_input():
    """
    Helper function to continue the game
    """
    input("> Press 'Enter' to continue")
    # to remove the input text above (works only for Unix-like os)
    print("\033[A                             \033[A")


def invalid_answer(validation_type):
    """
    Helper function to show error message
    """
    if validation_type == 'username':
        print('Name should be more than 1 symbol and less then 10\n')
    elif validation_type == 'yes_no':
        print("No such options. Your answer might be Y or N\n")
    elif validation_type == 'options':
        print("No such options. Choose it from the options list.\n")
    else:
        print('Something went wrong!')
    continue_input()


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
    """
    Function to show battle stats
    """
    enemy_stats = f'| {enemy.name.upper()} | {enemy.hp}/{enemy.max_hp} HP | {enemy.attack_dmg} DMG |\n'

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
            invalid_answer('username')


def prolog(player):
    """
    Function for game prolog
    """
    show_stats(player)
    print('You wake up in a dimly lit cave, the flickering light of a campfire casting shadows on the walls.')
    print('A mysterious figure sits across, tending the fire.\n\n')
    continue_input()
    show_stats(player)
    print(f'''Stranger:
        Ah, {player.username}, you stir at last.
        I heard a dragon's cry and found you lying at the mountain's base.
        You must've ventured to the summit, where the fabled Dragon dwells.
    ''')
    continue_input()
    show_stats(player)
    while True:
        print(f'''Stranger:
        This elixir will mend your wounds.
        *He extends a vial of glowing liquid*
        *Will you accept? (Y/N)*
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
            invalid_answer('yes_no')
            show_stats(player)


def battle(player, enemy):
    """
    Function the start the battle between player and enemy
    """
    while True:
        show_stats(player)
        battle_stats(enemy)
        print(f'1. Strike the {enemy.name}')
        print('2. Defend and Counter-Attack')
        print('3. Use Health Potion')

        choise = input('# ')

        if choise == '1':
            enemy.hp = max(0, enemy.hp - player.attack_dmg)
            if enemy.hp > 0:
                print(f'You strike {enemy.name}, dealing {player.attack_dmg} damage.')
                continue_input()
                print(f"{enemy.name} strikes back, dealing {enemy.attack_dmg} points of damage to you.")
                player.hp = max(0, player.hp - enemy.attack_dmg)
                continue_input()
                if player.hp > 0:
                    show_stats(player)
                    battle_stats(enemy)
                else:
                    return False
            else:
                show_stats(player)
                battle_stats(enemy)
                print(f'You strike {enemy.name}, dealing {player.attack_dmg} damage.')
                continue_input()
                print(f'You vanquish {enemy.name}, emerging victorious!')
                continue_input()
                return True
        elif choise == '2':
            # Add random chance to block damage from 1 to enemy damage
            print(f"You attempt to block the incoming attack from {enemy.name}.")
            continue_input()
            blocked_dmg = random.randint(1, enemy.attack_dmg)
            player.hp = max(0, player.hp + blocked_dmg - enemy.attack_dmg)
            print(f"Fortunately, you manage to block {blocked_dmg} damage.")
            continue_input()
            print(f'{enemy.name} retaliates, inflicting {enemy.attack_dmg - blocked_dmg} damage.')
            continue_input()
            # Add random chance to counter-attack the enemy
            if random.randint(1, 100) <= 30:
                print(f"Your counter-attack is successful, dealing {player.attack_dmg} damage to {enemy.name}.")
                enemy.hp = max(0, enemy.hp - player.attack_dmg)
                continue_input()
                if enemy.hp <= 0:
                    print(f'You vanquish {enemy.name}, emerging victorious!')
                    continue_input()
                    return True
            else:
                print("You attempt a counter-attack, but it fails to land.")
                continue_input()
            if player.hp <= 0:
                return False
        elif choise == '3':
            use_potion(player)
        else:
            invalid_answer('options')


def use_potion(player):
    if player.potions > 0:
        player.potions -= 1
        heal_amount = 30
        player.hp = min(player.max_hp, player.hp + heal_amount)
        print(f"You used a health potion and restored {heal_amount} HP.")
        continue_input()
    else:
        print("You don't have any health potions.")
        continue_input()


def game_over(player, enemy):
    """
    Function for game over
    """
    while True:
        text_align_center("|===================================|")
        text_align_center("|            GAME OVER              |")
        text_align_center("|===================================|\n")
        print(f'Well well.. {player.username}. You were defeated by {enemy.name}. So sad..\n')
        print('1. Go to main menu')
        print('2. Quit the game')

        choise = input('# ')
        if choise == '1':
            main_menu()
            break
        elif choise == '2':
            exit_game()
        else:
            invalid_answer('options')
            show_stats(player)
            battle_stats(enemy)


def cave_actions(player):
    """
    Function with actions for Cave location
    """
    show_stats(player)
    print('1. Exit the Cave')
    print('2. Scour the Cave')
    print('3. Talk to the Stranger')
    print('4. Use Health Potion')

    choise = input('# ')

    if choise == '1':
        player.location = 'Forest'
        show_stats(player)
        print('You venture forth into the Forest.\n')
        continue_input()
        forest_actions(player)
    elif choise == '2':

        if 'Cave' not in player.explored_locations:
            show_stats(player)
            print('You decide to delve deeper into the cave...')
            continue_input()
            print('A glint catches your eye.')
            print("It's a sack of gold coins!")
            print('*You acquire 10 coins!*')
            continue_input()
            player.coins += 10
            player.explored_locations.append('Cave')
            show_stats(player)
            cave_actions(player)
        else:
            show_stats(player)
            print('You feel you have uncovered all the cave’s secrets.\n')
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
    elif choise == '4':
        use_potion(player)
        cave_actions(player)
    else:
        invalid_answer('options')
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
            player.visited_locations.append('Forest')

            coins_found = random.randint(5, 20)
            player.coins += coins_found

            print(f"After searching, you found {coins_found} coins.")

            continue_input()
            forest_actions(player)

        else:
            show_stats(player)
            battle_stats(enemy_wolf)
            game_over(player, enemy_wolf)

    else:
        show_stats(player)
        print('1. Enter the Cave')
        print('2. Explore the Forest')
        print('3. Go to the Village')
        print('4. Use Health Potion')

        choise = input('# ')

        if choise == '1':
            player.location = 'Cave'
            show_stats(player)
            print('You are enter the Cave\n')
            continue_input()
            cave_actions(player)
        elif choise == '3':
            player.location = 'Village'
            show_stats(player)
            print('You go to the Village\n')
            continue_input()
            village_actions(player)
        elif choise == '4':
            use_potion(player)
            forest_actions(player)
        else:
            invalid_answer('options')
            forest_actions(player)


def village_actions(player):
    if 'Village' not in player.visited_locations:
        show_stats(player)
        player.visited_locations.append('Village')
        print("As you step into the village, you're greeted by the warm smiles of the villagers.")
        continue_input()
        print("Children are playing in the streets, and the aroma of freshly baked bread fills the air.")
        continue_input()
        print("A sense of community and peace envelops you.")
        continue_input()

    show_stats(player)
    print('1. Go to the Forest')
    print('2. Explore the Village')
    print('3. Go to the merchant')
    print('4. Go to the castle')
    print('5. Use Health Potion')

    choise = input('# ')

    if choise == '1':
        player.location = 'Forest'
        show_stats(player)
        print('You are enter the Forest\n')
        continue_input()
        forest_actions(player)
    elif choise == '5':
        use_potion(player)
        village_actions(player)
    else:
        invalid_answer('options')
        village_actions(player)


def show_rules():
    """
    Function to show rules of the game
    """
    terminal_width = shutil.get_terminal_size()[0]
    word = "RULES"

    num_dashes = terminal_width - len(word) - 2  # 2 for the spaces around word "RULES"
    dashes = num_dashes // 2
    remaining_dashes = num_dashes % 2  # In case the terminal width is odd
    rules_title = '-' * dashes + ' ' + word + ' ' + '-' * (dashes + remaining_dashes)
    
    ascii_art_logo()
    text_align_center(rules_title)
    print("1. You will be presented with a list of options at each stage of the game.")
    print("2. To make a choice, simply enter the number corresponding to the option you'd like to choose.")
    print("3. In battles, you can either attack or defend:")
    print("   - Attacking will deal damage to the enemy.")
    print("   - Defending will block some incoming damage and has a 30% chance to counter-attack.")
    text_align_center('-' * terminal_width)
    continue_input()
    main_menu()


def exit_game():
    """
    Function to exit the game
    """
    ascii_art_logo()
    text_align_center("===================================")
    text_align_center("|         FAREWELL, HERO          |")
    text_align_center("===================================")
    print("\nAs you step away from the world of adventure, the echoes of your deeds fade into legend.")
    print("May your path be clear, your sword sharp, and your courage unyielding.")
    print("Until we meet again, safe travels!\n")
    print("Goodbye, and thank you for playing!")
    quit()


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
    # elif choise == '2':
    #     pass
    elif choise == '3':
        show_rules()
    elif choise == '4':
        exit_game()
    else:
        print('No such options! Please select number from menu options. Press "Enter" to continue\n')
        continue_input()
        main_menu()


main_menu()
