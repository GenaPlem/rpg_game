import os
import shutil
import random
import uuid


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
        self.completed_quests = []
        self.forest_quest = False
        self.doomed_path_quest = False
        self.load_code = uuid.uuid4()

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

            if self.hp <= 0:
                return False

        else:
            print(f"You successfully parried the enemy's attack, taking no damage.")
            continue_input()

            # Add random chance to counter-attack the enemy
        if random.randint(1, 100) <= 35:
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
    """
    Class for forest wanderer
    """
    def __init__(self):
        super().__init__(name="Forest Wanderer", attack_dmg=12, max_hp=50)

        self.description = "A mysterious creature with dark fur and unsettling yellow eyes."
        self.is_alive = True

    def special_attack(self, player):
        special_dmg = int(self.attack_dmg * 1.3)
        print(f"{self.name} focuses its dark energy and unleashes a Shadow Strike, dealing {special_dmg} damage!")
        player.hp = max(0, player.hp - special_dmg)
        continue_input()

    def death_cry(self):
        print("As the Forest Wanderer falls, you feel as if a weight has been lifted from the forest.")
        self.is_alive = False
        continue_input()


class Ogre(Enemy):
    """
    Class for Ogre
    """
    def __init__(self):
        super().__init__(name="DoomBringer Ogre", attack_dmg=15, max_hp=80)

        self.description = "A hulking beast with thick, mottled skin and a club as large as a tree trunk."
        self.is_alive = True

    def special_attack(self, player):
        special_dmg = int(self.attack_dmg * 1.5)
        print(f"{self.name} roars and swings its massive club in a devastating arc, dealing {special_dmg} damage!")
        player.hp -= special_dmg
        continue_input()

    def death_cry(self):
        print("With a final, agonizing roar, the DoomBringer Ogre collapses, shaking the ground beneath you.")
        self.is_alive = False
        continue_input()


class Dragon(Enemy):
    """
    Class for Dragon, final boss
    """
    def __init__(self, player):
        # Calculate enemy stats based on player stats
        super().__init__(name="Ferocious Dragon", attack_dmg=30, max_hp=int(player.max_hp * 2))

        self.description = "A fearsome dragon with scales as hard as steel and breath as hot as fire."
        self.is_alive = True

    def special_attack(self, player):
        special_dmg = int(self.attack_dmg * 1.5)
        print(f"{self.name} unleashes its fiery breath, dealing {special_dmg} damage!")
        player.hp -= special_dmg
        continue_input()

    def death_cry(self):
        print("With a final roar, the dragon collapses, freeing the land from its reign of terror.")
        self.is_alive = False
        continue_input()


class Merchant:
    """
    Class for Merchant
    """
    def __init__(self):
        self.name = 'Mystic Merchant'

    def talk(self):
        print(f"{self.name}: Welcome to my Shop. You can buy potions and improve your attack damage.\n")
        continue_input()


class Quest:
    """
    Class for quest
    """
    def __init__(self, name, description, reward, is_completed):
        self.name = name
        self.description = description
        self.reward = reward
        self.is_completed = is_completed


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
        '  _____                              _       ______           ',
        '  |  __ \\                            ( )     |  ____|           ',
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
        print('Your name should be more than 1 symbol and less then 10. And it cant contains numbers\n')

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

        if 15 >= len(username.strip()) > 1 and username.isalpha():
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
                # If enemy have a special attack then he will use it with 25% chance
                if hasattr(enemy, 'special_attack') and random.randint(1, 100) <= 25:
                    enemy.special_attack(player)

                    if player.hp > 0:
                        show_stats(player)
                        battle_stats(enemy)

                    else:
                        return False

                else:
                    enemy.attack(player)

                if player.hp > 0:
                    show_stats(player)
                    battle_stats(enemy)

                else:
                    player.hp = 0
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
    """
    Function to use potion and restore HP
    """
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
        show_stats(player)
        battle_stats(enemy)
        text_align_center("|===================================|")
        text_align_center("|            GAME OVER              |")
        text_align_center("|===================================|\n")

        print(f'Well well.. {player.username}. You were defeated by {enemy.name}. So sad..')
        print(f"This is your code for Load Game: {player.load_code}")
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


def prolog(player):
    """
    Game Prolog
    """
    show_stats(player)
    print('You wake up in a dimly lit Cave, the flickering light of a campfire casting shadows on the walls.')
    print('A mysterious figure sits across, tending the fire.\n')
    continue_input()

    show_stats(player)
    print(f'Stranger: Ah, {player.username}, you stir at last.')
    print("I heard a dragon's cry and found you lying at the Mountain's base.")
    print("You must've ventured to the summit, where the fabled Dragon dwells.")
    print("If you're intent on facing the dragon again, please bring its eye to me! I would be grateful.\n")

    continue_input()

    show_stats(player)

    while True:
        print("Stranger: This elixir will mend your wounds.")
        print("*He extends a vial of glowing liquid*")
        print("*Will you drink it? (Y/N)*\n")

        drink_potion = input('# ').lower()

        if drink_potion == 'y':
            player.hp = player.max_hp

            show_stats(player)
            print(f'Your health now is {player.hp}/{player.max_hp}HP\n')
            print('Stranger: Good, now you are ready to go.')
            print("One more thing: if you want to get more Potions like this, just find the Merchant in the Village\n")

            continue_input()
            break

        elif drink_potion == 'n':
            show_stats(player)
            print("Stranger: As you say so...")
            print("By the way, if you are interested in survive, you have to find the Merchant in the Village\n")

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
        talk_to_stranger(player)
        cave_actions(player)

    elif choice == '4':
        use_potion(player)
        cave_actions(player)

    else:
        invalid_answer('options')
        cave_actions(player)


def explore_cave(player):
    """
    Function to explore the Cave
    """
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


def talk_to_stranger(player):
    """
    Function to talk to the Stranger
    """
    show_stats(player)
    if 'dragons_eye' in player.inventory:
        player.inventory.remove('dragons_eye')
        game_completion(player)
        main_menu()

    else:
        show_stats(player)
        print("Stranger: Ah, you're still here?")
        print("Time waits for no one, especially not in these treacherous lands. I suggest you move along.")
        print("I have my own matters to attend to.\n")
        continue_input()


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

            print(f"After searching, you found {coins_found} coins.\n")

            continue_input()
            forest_actions(player)

        else:
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


def explore_forest(player):
    """
    Function to explore the Forest
    """
    if 'Forest' not in player.explored_locations:
        if player.forest_quest:
            forest_wanderer = ForestWanderer()

            if forest_wanderer.is_alive:
                print("You venture deeper into the Forest, the air growing thicker and the trees towering above.\n")
            continue_input()
            if battle(player, forest_wanderer):
                player.inventory.append('villagers_amulet')
                player.explored_locations.append('Forest')
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

        print("A sense of community and peace envelops you.\n")
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
        if 'Forest Quest' not in player.completed_quests:
            talk_to_villager(player)
            village_actions(player)
        else:
            talk_to_villager(player)
            village_actions(player)

    elif choice == '5':
        player.location = 'Castle'

        show_stats(player)
        print('You step through the grand archway, entering the Castle.\n')
        continue_input()
        castle_actions(player)
    elif choice == '6':
        use_potion(player)
        village_actions(player)

    else:
        invalid_answer('options')
        village_actions(player)


def explore_village(player):
    """
    Function to explore the Village
    """
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
    if 'Forest Quest' not in player.completed_quests:
        if not player.forest_quest:
            forest_quest = Quest("Explore the Deep Forest",
                                 "Venture into the depths of the Forest and find the lost amulet.",
                                 50,
                                 False)

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
                    forest_quest = Quest("Explore the Deep Forest",
                                         "Venture into the depths of the Forest and find the lost amulet.",
                                         50,
                                         False)

                    show_stats(player)
                    print("Villager: Ah, you've found my amulet! Thank you so much!")
                    print("As promised, here is your reward.")
                    print(f"*Villager hands you a pouch of coins. (+{forest_quest.reward} coins)*\n")

                    player.coins += forest_quest.reward
                    player.completed_quests.append('Forest Quest')
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
    """
    Displays shop
    """
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


def castle_actions(player):
    """
    Castle's location actions
    """
    if 'Castle' not in player.visited_locations:
        player.visited_locations.append('Castle')

        show_stats(player)
        print("As you enter the castle gates, you feel a sense of grandeur.")
        continue_input()

        print("Stone walls tower above you, and the distant sound of clashing swords fills the air.\n")
        continue_input()

    show_stats(player)
    print('1. Return to the Village')
    print('2. Talk to the King')
    print('3. Speak with the Forge Master')
    print('4. Go to the Doomed Path')
    print('5. Drink Health Potion (+30HP)')

    choice = input('# ')

    if choice == '1':
        player.location = 'Village'

        show_stats(player)
        print('You step onto the worn path leading back to the Village.\n')
        continue_input()
        village_actions(player)

    elif choice == '2':
        talk_to_king(player)
        castle_actions(player)

    elif choice == '3':
        show_stats(player)
        forge_master(player)
        castle_actions(player)

    elif choice == '4':
        if not player.doomed_path_quest:
            show_stats(player)
            print("Guard: I can't let you pass, it's too dangerous beyond this point.\n")
            continue_input()
            castle_actions(player)

        elif 'Kings Quest' in player.completed_quests:
            show_stats(player)
            print('You step onto the Doomed Path.\n')
            continue_input()

            player.location = 'Doomed Path'
            doomed_path_actions(player)

        else:
            show_stats(player)
            print('Guard: Good luck, great warrior.\n')
            continue_input()
            player.location = 'Doomed Path'
            doomed_path_actions(player)

    elif choice == '5':
        use_potion(player)
        castle_actions(player)

    else:
        invalid_answer('options')
        castle_actions(player)


def talk_to_king(player):
    """
    Function to talk to the King and get a quest
    """
    show_stats(player)
    if 'Kings Quest' not in player.completed_quests:
        if not player.doomed_path_quest:
            kings_quest = Quest('Slay the Ogre on the Doomed Path',
                                'An ogre has been terrorizing the Doomed Path. Slay it and bring peace to the land.',
                                100,
                                False)

            print(f"King: Hey you! You appear before me just as a new task arises that requires... competence.")
            print("An ogre on the Doomed Path disrupts trade and endangers the village.")
            print("Would you be willing to slay it? The reward will be generous.\n")

            print(f"Quest: {kings_quest.name}")
            print(f"Description: {kings_quest.description}\n")
            print("Do you accept? (Y/N)")

            choice = input('# ').lower()

            if choice == 'y':
                show_stats(player)
                print("King: Brilliant! May fortune favor you on your quest.\n")
                continue_input()
                player.doomed_path_quest = True

            elif choice == 'n':
                show_stats(player)
                print("King: Hmph. Reconsider your decision, or find your way out of my presence.\n")
                continue_input()

            else:
                invalid_answer('yes_no')
                talk_to_king(player)
        else:
            print(f"King: Hey you, have you slain the ogre yet? (Y/N)\n")

            choice = input('# ').lower()

            if choice == 'y':

                if "ogre_head" in player.inventory:
                    kings_quest = Quest('Slay the Ogre on the Doomed Path',
                                        'Ogre has been terrorizing the Doomed Path Slay it and bring peace to the land',
                                        100,
                                        False)

                    show_stats(player)
                    print("King: You've done it! The Doomed Path is safe once more!")
                    print("As promised, here is your reward. A King's word is his bond.\n")
                    print(f"*The King gives you a hefty pouch of coins. (+{kings_quest.reward} coins)*\n")

                    player.coins += kings_quest.reward
                    player.completed_quests.append('Kings Quest')
                    player.inventory.remove("ogre_head")

                    player.inventory.append('hidden_upgrade_token')

                    continue_input()

                    kings_quest.is_completed = True

                    show_stats(player)
                    print("King: Visit my Forge Master")
                    print("I told him to make your armor better. And you can rest before leaving.\n")
                    continue_input()

                    castle_actions(player)

                else:
                    show_stats(player)
                    print('King: How dare you lie to your King? Return when the deed is done.')
                    print('*You feel a sense of shame*\n')
                    continue_input()
                    castle_actions(player)

            elif choice == 'n':
                show_stats(player)
                print("King: Time is of the essence. Please hurry.\n")
                continue_input()

            else:
                invalid_answer('yes_no')
                talk_to_king(player)
    else:
        print("King: You've done a great service to the kingdom. Thank you!\n")
        continue_input()


def forge_master(player):
    """
    Function to talk to forge master
    """
    show_stats(player)
    if "hidden_upgrade_token" in player.inventory:
        print(f'Forge Master: Ah, {player.username}, your deeds have not gone unnoticed.')
        print("Hand over your armor. I'll fortify it for you.")
        print('While you wait, You can rest and heal your wounds\n')

        player.max_hp += 50
        player.hp = player.max_hp
        player.inventory.remove("hidden_upgrade_token")
        continue_input()

    else:
        print("Forge Master: I'm busy right now. Come back later.\n")
        continue_input()


def doomed_path_actions(player):
    """
    Function to handle actions in the Path of the Doomed
    """
    if 'Doomed Path' not in player.visited_locations:
        player.visited_locations.append('Doomed Path')

        show_stats(player)
        ogre = Ogre()

        print("As soon as you step into the Doomed Path")
        print("The Ogre attack you. And the battle begins\n")
        continue_input()

        if battle(player, ogre):
            print('*You cut Ogres Head*\n')
            player.inventory.append('ogre_head')
        else:
            game_over(player, ogre)
        continue_input()

    show_stats(player)
    print('1. Return to the Castle')
    print('2. Look around')
    print('3. Climb to the Mountain Peak')
    print('4. Drink Health Potion (+30HP)')

    choice = input('# ')

    if choice == '1':
        player.location = 'Castle'

        show_stats(player)
        print("You've returned to the Castle from the Doomed Path.\n")
        continue_input()
        castle_actions(player)

    elif choice == '2':
        show_stats(player)
        explore_doomed_path(player)

    elif choice == '3':
        show_stats(player)
        print('This is a way to the Dragon. Are you strong enough? (Y/N)')

        choice = input('# ').lower()

        if choice == 'y':
            player.location = 'Mountain Peak'

            show_stats(player)
            print('You Climb The Mountain\n')
            continue_input()
            mountain_actions(player)

        elif choice == 'n':
            show_stats(player)
            print("No one escape him yet. Prepare yourself well.\n")
            continue_input()
            doomed_path_actions(player)

        else:
            invalid_answer('yes_no')

    elif choice == '4':
        use_potion(player)
        doomed_path_actions(player)

    else:
        invalid_answer('options')
        doomed_path_actions(player)


def explore_doomed_path(player):
    """
    Function to look around the Doomed Path
    """
    if 'Doomed Path' not in player.explored_locations:
        show_stats(player)
        print('You decide to explore the area where the Ogre used to roam...\n')
        continue_input()

        money_bag = random.randint(30, 50)
        player.potions += 1

        print("As you sift through the debris and remnants of the Ogre's lair, your eyes catch a glint.")
        print("It's a small stash of gold coins, likely plundered by the Ogre!")
        print(f'*You acquire {money_bag} coins! And found 1 Potion*\n')
        continue_input()

        player.coins += money_bag
        player.explored_locations.append('Doomed Path')

        show_stats(player)
        print("Feeling a bit richer and more relieved that the Ogre is no more, you ponder your next move.\n")
        continue_input()
        doomed_path_actions(player)
    else:
        show_stats(player)
        print("You've already explored the Doomed Path thoroughly and claimed its hidden treasures.")
        print("Perhaps it's time to seek new adventures.\n")
        continue_input()
        doomed_path_actions(player)


def mountain_actions(player):
    """
    Function to handle actions on the Mountain Peak
    """
    if 'Mountain Peak' not in player.visited_locations:
        player.visited_locations.append('Mountain Peak')

        show_stats(player)
        dragon = Dragon(player)

        print("Mountain Peak is near")
        print("You've heard a Dragons Roar and he starts flying to you\n")
        continue_input()

        if battle(player, dragon):
            print('*You extract Dragons Eye*\n')
            player.inventory.append('dragons_eye')
        else:
            game_over(player, dragon)
        continue_input()

    show_stats(player)
    print('1. Go down to the Doomed Path')
    print('2. Look around')
    print('3. Drink Health Potion (+30HP)')

    choice = input('# ')

    if choice == '1':
        player.location = 'Doomed Path'

        show_stats(player)
        print("You've returned to the Doomed Path.\n")
        continue_input()
        doomed_path_actions(player)

    elif choice == '2':
        show_stats(player)
        explore_mountain_peak(player)

    elif choice == '3':
        use_potion(player)
        mountain_actions(player)

    else:
        invalid_answer('options')
        mountain_actions(player)


def explore_mountain_peak(player):
    """
    Function to look around on the Mountains Peak
    """
    if 'Mountain Peak' not in player.explored_locations:
        show_stats(player)
        print('You stand over the defeated dragon, its remaining eye staring lifelessly into the void.\n')
        continue_input()

        print("A sense of accomplishment washes over you. Your journey, fraught with peril, has come to an end.")
        print("You've conquered the Mountain Peak and vanquished the dragon that terrorized these lands.")
        continue_input()

        show_stats(player)
        print("As you prepare to leave, you remember the Dragon's Eye you've taken.")
        print("The Stranger who aided you at the beginning of your journey might find it valuable.")
        print("Perhaps it's time to pay him a visit and bring closure to your adventure.\n")
        continue_input()

        player.explored_locations.append('Mountain Peak')

        show_stats(player)
        print("Feeling victorious and fulfilled, you ponder your next move.\n")
        continue_input()
        mountain_actions(player)

    else:
        show_stats(player)
        print("You've already explored the Mountain Peak thoroughly and claimed its hidden treasures.")
        print("Perhaps it's time to seek new adventures.\n")
        continue_input()
        mountain_actions(player)


def game_completion(player):
    """
    Game complete function
    """
    show_stats(player)
    print("As you hand over the dragon's eye to the Stranger, a sense of finality washes over you.")
    continue_input()

    print("The Stranger smiles, 'You've done it. You've not only defeated the dragon but also fulfilled a destiny.'")
    continue_input()

    print("'The villagers may never know the full extent of your heroism, but their lives are better because of you.'")
    continue_input()

    print("You realize that your adventure has come to an end, but the legends of your bravery will echo through time.")
    continue_input()

    print("The Stranger adds, 'Who knows, maybe our paths will cross again in another life, another adventure.'")
    continue_input()

    print("As you step out of the cave, back into the world you've saved, you can't help but wonder what's next.")
    continue_input()

    print("Thank you for playing! Your adventure has come to an end, but the future is an open book.")
    continue_input()


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
