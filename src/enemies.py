import random

enemy_list = []

class Enemy:
    def __init__(self, x, y, hp, dmg) -> None:
        self.x = x
        self.y = y
        self.hp = hp
        self.dmg = dmg
    
    def spawn_enemy(self):
        print("Spawned enemy")

class Slime(Enemy):
    def __init__(self, name, x, y, hp, dmg) -> None:
        super().__init__(x, y, hp, dmg)
        self.name = name
        self.look = "!"
    
    def spawn_enemy(self):
        print("Spawned slime")


