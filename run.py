class Player:
    def __init__(self, username):
        self.username = username
        self.attack_dmg = 10
        self.hp = 20
        self.max_hp = 50
        self.coins = 0
        self.potions = 0
        self.inventory = []


def initialize_game():
    username = input('Enter your Name! ')
    new_user = Player(username)
    print(f" Hey, {new_user.username}. You finally awake! Hope you're fine.")


initialize_game()
