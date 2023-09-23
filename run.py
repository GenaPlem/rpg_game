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
        self.forest_quest = False

    def attack(self, enemy):
        enemy.hp = max(0, enemy.hp - self.attack_dmg)
        print(f'You strike {enemy.name}, dealing {self.attack_dmg} damage.')
        continue_input()

    def block(self, enemy):
        print(f"You attempt to block the incoming attack from {enemy.name}.")
        continue_input()

        # Add random chance to block damage from 1 to enemy damage
        blocked_dmg = random.randint(1, enemy.attack_dmg)
        self.hp = max(0, self.hp + blocked_dmg - enemy.attack_dmg)

        print(f"Fortunately, you manage to block {blocked_dmg} damage.")
        continue_input()

        if blocked_dmg != enemy.attack_dmg:
            print(f'{enemy.name} retaliates, inflicting {enemy.attack_dmg - blocked_dmg} damage.')
            continue_input()

        else:
            print(f"You successfully parried the enemy's attack, taking no damage.")
            continue_input()

            # Add random chance to counter-attack the enemy
        if random.randint(1, 100) <= 30:
            print(f"Your counter-attack is successful, dealing {self.attack_dmg} damage to {enemy.name}.")

            enemy.hp = max(0, enemy.hp - self.attack_dmg)
            continue_input()

            if enemy.hp <= 0:
                show_stats(self)
                battle_stats(enemy)
                print(f'You vanquish {enemy.name}, emerging victorious!')
                continue_input()

                return True

        else:
            print("You attempt a counter-attack, but it fails to land.")
            continue_input()

    def win(self, enemy):
        show_stats(self)
        battle_stats(enemy)
        print(f'You vanquish {enemy.name}, emerging victorious!')
        continue_input()


class Enemy:
    """
    Class for enemy
    """
    def __init__(self, name, attack_dmg, max_hp):
        self.name = name
        self.attack_dmg = attack_dmg
        self.max_hp = max_hp
        self.hp = self.max_hp

    def attack(self, player):
        player.hp = max(0, player.hp - self.attack_dmg)
        print(f"{self.name} strikes back, dealing {self.attack_dmg} points of damage to you.")
        continue_input()


class ForestWanderer(Enemy):
    def __init__(self):
        # Calculate enemy stats based on player stats
        super().__init__(name="Forest Wanderer", attack_dmg=12, max_hp=50)

        self.description = "A mysterious creature with dark fur and unsettling yellow eyes."
        self.reward = 50
        self.is_alive = True

    def special_attack(self, player):
        special_dmg = self.attack_dmg * 1.5
        print(f"{self.name} focuses its dark energy and unleashes a Shadow Strike, dealing {special_dmg} damage!")
        player.hp -= special_dmg
        continue_input()

    def death_cry(self):
        print("As the Forest Wanderer falls, you feel as if a weight has been lifted from the forest.")
        self.is_alive = False
        continue_input()


class Merchant:
    def __init__(self):
        self.name = 'Seraphina the Mystic Merchant'

    def talk(self):
        print(f"{self.name}: Welcome to my Shop. You can buy potions and improve your attack damage.\n")
        continue_input()


class Quest:
    """
    Class for quest
    """
    def __init__(self, name, description, reward):
        self.name = name
        self.description = description
        self.reward = reward
        self.is_completed = False


def clear():
    """
    Helper function to clear the terminal
    """
    os.system('clear')


def ascii_art_logo():
    """
    Displays ascii art logo
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
    terminal_width = shutil.get_terminal_size()[0]

    for line in ascii_art:
        padding = (terminal_width - len(line)) // 2
        print(' ' * padding + line)


def text_align_center(text):
    """
    Centralize text
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
    Displays choice error message
    """
    if validation_type == 'username':
        print('Name should be more than 1 symbol and less then 10\n')

    elif validation_type == 'yes_no':
        print("No such options. Your answer might be Y or N\n")

    elif validation_type == 'options':
        print("No such options. Choose it from the options list.\n")

    elif validation_type == 'menu':
        print('No such options! Please select number from menu options.\n')

    else:
        print('Something went wrong!')

    continue_input()


def show_stats(player):
    """
    Displays stats of player
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
    Displays battle stats
    """
    enemy_stats = f'| {enemy.name.upper()} | {enemy.hp}/{enemy.max_hp} HP | {enemy.attack_dmg} DMG |\n'

    max_length = len(enemy_stats) - 1
    num_symbols = max_length - len('Battle') - 2

    title = '|' + '=' * num_symbols + ' Battle ' + '=' * num_symbols + '|'

    text_align_center(title)
    text_align_center(enemy_stats)


def initialize_game():
    """
    Initialize the game after creating a new player
    """
    while True:
        ascii_art_logo()

        username = input('Enter your name Hero! \n')

        if 15 >= len(username.strip()) > 1:
            player = Player(username)
            return player
        else:
            invalid_answer('username')


def battle(player, enemy):
    """
    Starts the battle between player and enemy
    """
    while True:
        show_stats(player)
        battle_stats(enemy)

        print(f'1. Strike the {enemy.name}')
        print('2. Defend and Counter-Attack')
        print('3. Drink Health Potion (+30HP)')

        choice = input('# ')

        if choice == '1':
            player.attack(enemy)

            if enemy.hp > 0:
                enemy.attack(player)

                if player.hp > 0:
                    show_stats(player)
                    battle_stats(enemy)

                else:
                    return False

            else:
                player.win(enemy)
                return True

        elif choice == '2':
            player.block(enemy)

            if enemy.hp <= 0:
                return True

            if player.hp <= 0:
                return False

        elif choice == '3':
            use_potion(player)

        else:
            invalid_answer('options')


def use_potion(player):
    if player.potions > 0:

        if player.hp != player.max_hp:
            player.potions -= 1
            heal_amount = 30
            player.hp = min(player.max_hp, player.hp + heal_amount)

            print(f"You used a health potion and restored {heal_amount} HP.\n")
            continue_input()

        else:
            print('You already have full HP!\n')
            continue_input()

    else:
        print("You don't have any health potions.\n")
        continue_input()


def game_over(player, enemy):
    """
    Game over function
    """
    while True:
        text_align_center("|===================================|")
        text_align_center("|            GAME OVER              |")
        text_align_center("|===================================|\n")

        print(f'Well well.. {player.username}. You were defeated by {enemy.name}. So sad..\n')
        print('1. Go to Main Menu')
        print('2. Quit the Game')

        choice = input('# ')

        if choice == '1':
            main_menu()
            break

        elif choice == '2':
            exit_game()

        else:
            invalid_answer('options')
            show_stats(player)
            battle_stats(enemy)


def prolog(player):
    """
    Game Prolog
    """
    show_stats(player)
    print('You wake up in a dimly lit Cave, the flickering light of a campfire casting shadows on the walls.')
    print('A mysterious figure sits across, tending the fire.\n')
    continue_input()

    show_stats(player)
    print(f'''Stranger:
        Ah, {player.username}, you stir at last.
        I heard a dragon's cry and found you lying at the Mountain's base.
        You must've ventured to the summit, where the fabled Dragon dwells.
    ''')
    continue_input()

    show_stats(player)

    while True:
        print(f'''Stranger:
        This elixir will mend your wounds.
        *He extends a vial of glowing liquid*
        *Will you drink it? (Y/N)*
    ''')

        drink_potion = input('# ').lower()

        if drink_potion == 'y':
            player.hp = player.max_hp

            show_stats(player)
            print(f'Your health now is {player.hp}/{player.max_hp}HP\n')
            print('''Stranger:
            Good, now you are ready to go.
            One more thing: if you want to get more Potions like this, just find the Merchant in the Village
            ''')
            continue_input()
            break

        elif drink_potion == 'n':
            show_stats(player)
            print('''Stranger:
            As you say so...
            By the way, if you are interested in survive, you have to find the Merchant in the Village
            ''')
            continue_input()
            break

        else:
            invalid_answer('yes_no')
            show_stats(player)


def cave_actions(player):
    """
    Displays actions for Cave location
    """
    show_stats(player)
    print('1. Leave the Cave')
    print('2. Explore the Cave')
    print('3. Talk to the Stranger')
    print('4. Drink Health Potion (+30HP)')

    choice = input('# ')

    if choice == '1':
        player.location = 'Forest'

        show_stats(player)
        print('You venture forth into the Forest.\n')
        continue_input()
        forest_actions(player)

    elif choice == '2':
        explore_cave(player)

    elif choice == '3':
        show_stats(player)
        print('''Stranger:
        Ah, you're still here?
        Time waits for no one, especially not in these treacherous lands. I suggest you move along.
        I have my own matters to attend to.
        ''')
        continue_input()
        cave_actions(player)

    elif choice == '4':
        use_potion(player)
        cave_actions(player)

    else:
        invalid_answer('options')
        cave_actions(player)


def explore_cave(player):
    if 'Cave' not in player.explored_locations:
        show_stats(player)
        print('You decide to delve deeper into the Cave...\n')
        continue_input()

        print('A glint catches your eye.')
        print("It's a sack of gold coins!")
        print('*You acquire 10 coins!*\n')
        continue_input()

        player.coins += 10
        player.explored_locations.append('Cave')

        show_stats(player)
        cave_actions(player)

    else:
        show_stats(player)
        print("You've uncovered all the Cave's secrets.\n")
        continue_input()
        cave_actions(player)


def forest_actions(player):
    """
    Displays actions in Forest location
    """
    if 'Forest' not in player.visited_locations:
        enemy_wolf = Enemy('Wolf', 5, 40)

        show_stats(player)
        print('As you step out of the Cave, you feel the fresh air and sun on your face.')
        print('Suddenly, a low growl comes from the bushes. A ferocious Wolf lunges at you.\n')
        continue_input()

        print('You were attacked by a Wolf')
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

        print('1. Venture into the Cave')
        print('2. Explore the Forest')
        print('3. Head to the Village')
        print('4. Drink Health Potion (+30HP)')

        choice = input('# ')

        if choice == '1':
            player.location = 'Cave'

            show_stats(player)
            print('You are enter the Cave\n')
            continue_input()
            cave_actions(player)

        elif choice == '2':
            show_stats(player)
            explore_forest(player)

        elif choice == '3':
            player.location = 'Village'

            show_stats(player)
            print('You go to the Village\n')
            continue_input()
            village_actions(player)

        elif choice == '4':
            use_potion(player)
            forest_actions(player)

        else:
            invalid_answer('options')
            forest_actions(player)


forest_wanderer = ForestWanderer()


def explore_forest(player):
    """
    Function to explore the Forest
    """
    if player.forest_quest and forest_wanderer.is_alive:
        print("You venture deeper into the Forest, the air growing thicker and the trees towering above.\n")
        continue_input()
        if battle(player, forest_wanderer):
            player.inventory.append('villagers_amulet')
            forest_wanderer.death_cry()

            print("After a brief search, you find the lost amulet deep within the forest.")
            print("It's time to return it to its rightful owner in the village.\n")
            continue_input()
            forest_actions(player)

        else:
            game_over(player, forest_wanderer)

    else:
        print("You wander around the Forest for a while but find nothing more than small critters.\n")
        continue_input()
        forest_actions(player)


def village_actions(player):
    """
    Displays actions for Village location
    """
    if 'Village' not in player.visited_locations:
        player.visited_locations.append('Village')

        show_stats(player)
        print("As you step into the Village, you're greeted by the warm smiles of the villagers.")
        continue_input()

        print("Children are playing in the streets, and the aroma of freshly baked bread fills the air.")
        continue_input()

        print("A sense of community and peace envelops you.")
        continue_input()

    show_stats(player)
    print('1. Venture into the Forest')
    print('2. Wander Around the Village')
    print('3. Visit the Merchant')
    print('4. Talk to the Villager')
    print('5. Approach the Castle')
    print('6. Drink Health Potion (+30HP)')

    choice = input('# ')

    if choice == '1':
        player.location = 'Forest'

        show_stats(player)
        print('You are enter the Forest\n')
        continue_input()
        forest_actions(player)

    elif choice == '2':
        explore_village(player)

    elif choice == '3':
        show_stats(player)
        print('You are enter the Shop\n')
        continue_input()
        shop(player)

    elif choice == '4':
        talk_to_villager(player)
        village_actions(player)

    elif choice == '6':
        use_potion(player)
        village_actions(player)

    else:
        invalid_answer('options')
        village_actions(player)


forest_quest = Quest("Explore the Deep Forest",
                     "Venture into the depths of the Forest and find the lost amulet.",
                     50)


def explore_village(player):
    if 'Village' not in player.explored_locations:
        show_stats(player)
        print('You decide to wander through the narrow streets of the Village...\n')
        continue_input()

        money_bag = random.randint(15, 30)

        print('As you stroll, you notice something shiny wedged between the cobblestones.')
        print("It's a small bag of coins, seemingly forgotten or lost!")
        print(f'*You acquire {money_bag} coins!*\n')
        continue_input()

        player.coins += money_bag
        player.explored_locations.append('Village')

        show_stats(player)
        print("Feeling a bit richer and more familiar with the Village, you ponder your next move.\n")
        continue_input()
        village_actions(player)

    else:
        show_stats(player)
        print("You've already explored the Village thoroughly and found its hidden treasures.")
        print("Perhaps it's time to seek new adventures.\n")
        continue_input()
        village_actions(player)


def talk_to_villager(player):
    """
    Function to talk to the villager and get a quest
    """
    show_stats(player)
    if not forest_quest.is_completed:
        if not player.forest_quest:

            print(f"Villager: Ah, {player.username}, you look like someone who could help us.")
            print("I've lost a precious amulet in the Deep Forest. It's been in my family for generations.")
            print("I would go myself, but the forest is too dangerous and filled with creatures.")
            print("Would you be willing to help me retrieve it? The reward will be generous.\n")

            print(f"Quest: {forest_quest.name}")
            print(f"Description: {forest_quest.description}\n")
            print("Do you accept? (Y/N)")

            choice = input('# ').lower()
            if choice == 'y':
                show_stats(player)
                print("Villager: Excellent! Good luck!\n")
                continue_input()
                player.forest_quest = True

            elif choice == 'n':
                show_stats(player)
                print("Villager: Oh, that's too bad. Maybe some other time then.\n")
                continue_input()

            else:
                invalid_answer('yes_no')
                talk_to_villager(player)
        else:
            print(f"Villager: Ah, {player.username}, have you found my amulet yet? (Y/N)\n")

            choice = input('# ').lower()

            if choice == 'y':

                if "villagers_amulet" in player.inventory:
                    show_stats(player)
                    print("Villager: Ah, you've found my amulet! Thank you so much!")
                    print("As promised, here is your reward.")
                    print(f"*Villager hands you a pouch of coins. (+{forest_quest.reward} coins)*\n")

                    player.coins += forest_quest.reward
                    player.inventory.remove("villagers_amulet")
                    continue_input()

                    forest_quest.is_completed = True
                    village_actions(player)

                else:
                    show_stats(player)
                    print('Villager: Deception? In my village? You best not be lying.')
                    print('*You feel a sense of shame*\n')
                    continue_input()
                    village_actions(player)

            elif choice == 'n':
                show_stats(player)
                print("Villager: I see. Please hurry, it means a lot to me.\n")
                continue_input()

            else:
                invalid_answer('yes_no')
                talk_to_villager(player)
    else:
        print("Villager: Thanks a lot. You've done that for us!\n")
        continue_input()


def shop(player):
    player.location = 'Shop'
    show_stats(player)
    merchant = Merchant()

    if 'Shop' not in player.visited_locations:
        merchant.talk()

    player.visited_locations.append('Shop')

    show_stats(player)
    print('1. Buy the Potion => 15 coins')
    print('2. Upgrade your Weapon (+5 DMG) => 25 coins')
    print('3. Leave the Shop')

    choice = input('# ')

    if choice == '1':
        if player.coins >= 15:
            player.coins -= 15
            player.potions += 1

            show_stats(player)
            print("Health Potions successfully purchased.\n")
            continue_input()
            shop(player)

        else:
            show_stats(player)
            print('Looks like you have not enough money!\n')
            continue_input()
            shop(player)
    elif choice == '2':
        if player.coins >= 25:
            player.coins -= 25
            player.attack_dmg += 5

            show_stats(player)
            print("Your Weapon successfully Upgraded.\n")
            continue_input()
            shop(player)

        else:
            show_stats(player)
            print('Looks like you have not enough money!\n')
            continue_input()
            shop(player)
    elif choice == '3':
        show_stats(player)
        print('You leave the Shop\n')
        continue_input()

        player.location = 'Village'
        village_actions(player)
    else:
        invalid_answer('options')
        shop(player)


def show_rules():
    """
    Displays Rules of the Game
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
    Exit the game
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
    Displays main menu
    """
    ascii_art_logo()

    text_align_center("1. New Game")
    text_align_center("2. Load Game")
    text_align_center("3. Rules")
    text_align_center("4. Quit")

    choice = input('# ')

    if choice == '1':
        player = initialize_game()
        prolog(player)
        cave_actions(player)

    # elif choice == '2':
    #     pass

    elif choice == '3':
        show_rules()

    elif choice == '4':
        exit_game()

    else:
        invalid_answer('menu')
        main_menu()


main_menu()
