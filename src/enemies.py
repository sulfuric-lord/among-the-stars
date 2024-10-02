class Enemy:
    def __init__(self, name, x, y, hp, dmg) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.hp = hp
        self.dmg = dmg
        self.look = "!"
    
#FIXME: Сделай так короче, чтоб была пошаговая система, владик из будущего
#ебись с этим сам
#А я пошел делать чет другое