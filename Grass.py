from Globals import *

class Grass(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 16, 16, (255, 0, 0), "../Images/Grass.png")
