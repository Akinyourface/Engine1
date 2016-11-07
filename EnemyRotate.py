from Globals import *


class EnemyRotate(Actor):
    def __init__(self, startx, starty):
        super().__init__(startx, starty, 24, 24)

    def _update(self, player):
        self.rotation = math.atan2(self.rect.y-player.rect.y, player.rect.x-self.rect.x)
        #self.image = pygame.transform.rotate(self.imageS, math.degrees(self.rotation))

        self.toPlayerX = player.rect.x - self.rect.x
        self.toPlayerY = player.rect.y - self.rect.y
        self.playerDis = int(math.sqrt(self.toPlayerX * self.toPlayerX + self.toPlayerY * self.toPlayerY))

        if self.playerDis <= 200:
            self.image = pygame.transform.rotate(self.imageS, math.degrees(self.rotation))

    
