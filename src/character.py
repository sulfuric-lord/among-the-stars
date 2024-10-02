import items

class Character:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.look = "@"
        self.might = 1
        self.dex = 1
        self.intt = 1
        self.hp = 25
        self.exp = 0
        self.level = 1
        self.weapon = items.hands
        

player = Character(1, 1)

