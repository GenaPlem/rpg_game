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


def main_menu():
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
        pass
    elif choise == '4':
        quit()
    else:
        main_menu()
        print('No such options! Please select number from menu options')


main_menu()
