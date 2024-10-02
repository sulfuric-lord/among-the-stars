import random
import character
import generators

class Item:
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y

class Weapon (Item):
    def __init__(self, name, x, y, _type, min_dmg, max_dmg) -> None:
        super().__init__(name, x, y)
        self._type = _type
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg 
    
    def pick_up(self):
        character.player.weapon = self
        generators.item_on_ground.remove(self)
        

#Стартовое оружие:
hands = Weapon("Hands", 0, 0, "can_wear", 0, 2)

iron_sword = Weapon("Iron sword", random.randint(1, 28), random.randint(1, 28), "can_wear", 5, 10)
