from Globals import *

class Enemy(Actor):
    def __init__(self, startX, startY):
        super().__init__(startX, startY, 16, 16, (2, 255, 255))
        super().register_subclass("Enemy")
        self.speed = 2
        self.stopMoving = False
        self.state = 0
    
    def _update(self, player):
        
        self.rotation = math.atan2(player.rect.y - self.rect.y, player.rect.x - self.rect.x)

        self.newRot = int(math.degrees(self.rotation))
    
        self.imageS = pygame.transform.rotate(self.image, self.newRot)
        
        
        self.toPlayerX = player.rect.x - self.rect.x
        self.toPlayerY = player.rect.y - self.rect.y
        self.playerDis = math.sqrt(self.toPlayerX * self.toPlayerX + self.toPlayerY * self.toPlayerY)
        self.toPlayerX = self.toPlayerX / self.playerDis
        self.toPlayerY = self.toPlayerY / self.playerDis


        if self.playerDis <= 250:
            self.state = 1
            self.speed = 7
        else:
            self.state = 0
            self.speed = 2
    
        if self.state == 1: #chasing        
            self.rect.x += math.cos(self.rotation) * self.speed
            self.rect.y += math.sin(self.rotation) * self.speed
        else:
            # maybe random movement?
            self.rect.x += 1



        
            
