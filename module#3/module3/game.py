from exceptions import GameOver
from models import Enemy, Player

print('RULES: start - start game, quit - leave game, magic = 1, warrior = 2, robber =3, magic > warrior > robber > magic')
start = input("If you want to start the game write 'start': ")
name = str(input("Enter your name: "))
player_obj = Player(name)

def play():
    level = 1
    enemy_obj = Enemy(level)
    while enemy_obj.level != 5:
        player_obj.attack(enemy_obj)
        player_obj.defence(enemy_obj)
        if enemy_obj.lives <= 0:
            level += 1
            enemy_obj = Enemy(level)
            player_obj.score += 5
            print("Level Up!")

if start == "start":
    if __name__ == "__main__":
        try:
            play()
        except GameOver:
            print(f"Ваш счет: {player_obj.score}")
            print("Game Over")
        except KeyboardInterrupt:
            pass
        finally:
            print("Good Bye!")
            exit()
elif start == 'quit':
    print('Bye')
    exit()
    



            