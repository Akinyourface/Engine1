from Globals import *



class Wall(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 16, 16, (0, 0, 0), "../Images/wall.png")
        
