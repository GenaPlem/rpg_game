class Player:
    def __init__(self, username, attack_dmg, heath_points, coins):
        self.username = username
        self.attack_dmg = attack_dmg
        self.heath_points = heath_points
        self.coins = coins


def initialize_game():
    username = input('Enter your Name! ')
    new_user = Player(username, 10, 100, 0)
    print(f" Hey, {new_user.username}. You finally awake! Hope you're fine.")


initialize_game()
