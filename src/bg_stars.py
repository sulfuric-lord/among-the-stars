import random

star_list = []

class Stars:
    def __init__(self, xpos, ypos, size):
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.color_value = 5
        self.color = (self.color_value, self.color_value, self.color_value)
        self.fading = False
        
    def shine(self):
        if self.color_value < 100 and not self.fading:
            self.color_value += 1
            self.color = (self.color_value, self.color_value, self.color_value)
        else:
            self.color = (self.color_value, self.color_value, self.color_value)
            self.fading = True
            self.color_value -= 0.2
            if self.color_value <= 0:
                star_list.remove(self)