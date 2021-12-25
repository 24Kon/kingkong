from random import randint
from exceptions import EnemyDown, GameOver
from settings import Const


def select_attack():
    return randint(1, 3)

def fight(attack, defence):
    if attack == defence:
        return 0
    elif attack > defence:
        return 1
    else:
        return -1

class Enemy:
    def __init__(self, lives):
        self.level = lives
        self.lives = lives

    def decrease_lives(self):
        if self.lives == 0:
            raise EnemyDown
        else:
            self.lives -= 1
            return self.lives

class Player:
    def __init__(self, name):
        self.name = name
        self.lives = Const.heal    # from settings.py
        self.score = 0

    def attack(self, enemy_obj):
        player_choice = int(input("You are attacking. Enter the number of your role: ")) # from settings.py
        enemy_choice = select_attack()
        if fight(player_choice, enemy_choice) == 0:
            print("It's a draw!")
        elif fight(player_choice, enemy_choice) == 1:
            enemy_obj.decrease_lives()
            self.score += 1
            print("You attacked successfully!")
        else:
            print("You missed!")

    def defence(self, enemy_obj):
        enemy_choice = select_attack()
        player_choice = int(input("You are defending. Enter the number of your role: ")) # from settings.py
        if fight(player_choice, enemy_choice) == 0:
            print("It's a draw!")
        elif fight(player_choice, enemy_choice) == 1:
            print("You defended successfully!")
        else:
            self.decrease_lives()
            print("You missed!")

    def decrease_lives(self):
        if self.lives <= 0:
            raise GameOver
        else:
            self.lives -= 1
            return self.lives