from Globals import *
from random import randint

class Enemyfollow(Actor):
    def __init__(self, startX, startY):
        super().__init__(startX, startY, 16, 16, (2, 255, 255))
        super().register_subclass("Enemy")
        self.speed = 2
        self.stopMoving = False
        self.state = 0
        self.dir = 4
        self.changedir = 0
        
    
    def _update(self, player):
        
        self.rotation = math.atan2(player.rect.y - self.rect.y, player.rect.x - self.rect.x)

        self.newRot = int(math.degrees(self.rotation))
    
        self.imageS = pygame.transform.rotate(self.image, self.newRot)
        
        
        self.toPlayerX = player.rect.x - self.rect.x
        self.toPlayerY = player.rect.y - self.rect.y
        self.playerDis = math.sqrt(self.toPlayerX * self.toPlayerX + self.toPlayerY * self.toPlayerY)
        self.toPlayerX = self.toPlayerX / self.playerDis
        self.toPlayerY = self.toPlayerY / self.playerDis
        self.wall_collide = pygame.sprite.spritecollide(self, self.walls, False)
        self.player_collide = pygame.sprite.spritecollide(self, self.player, False)

        if self.playerDis <= 250:
            self.speed = 7
            self.rect.x += math.cos(self.rotation) * self.speed
            self.rect.y += math.sin(self.rotation) * self.speed
            
        elif self.playerDis >= 250:
           
            if self.changedir == 50:
                self.dir = randint(1, 4)
                self.changedir = 0
            else:
                self.changedir += 1
            self.speed = 2
            #self.wall_collide = pygame.sprite.spritecollide(self, self.walls, False)
            #self.player_collide = pygame.sprite.spritecollide(self, self.player, False)
            for col in self.wall_collide:                
                if self.dir == 1:
                    self.dir = 2
                elif self.dir == 2:
                    self.dir = 1
                if self.dir == 3:
                    self.dir = 4
                elif self.dir == 4:
                    self.dir = 3
                
            if self.dir == 1:
                self.rect.x -= self.speed
            elif self.dir == 2:
                self.rect.x += self.speed
            elif self.dir == 3:
                self.rect.y -= self.speed
            elif self.dir == 4:
                self.rect.y += self.speed




















            
        """    self.state = 1
            self.speed = 7
        else:
            self.state = 0
            self.speed = 2
    
        if self.state == 1: #chasing        
            self.rect.x += math.cos(self.rotation) * self.speed
            self.rect.y += math.sin(self.rotation) * self.speed
        else:
            # maybe random movement?
            self.wall_collide = pygame.sprite.spritecollide(self, self.walls, False)
            self.player_collide = pygame.sprite.spritecollide(self, self.player, False)


            for col in self.player_collide:
                print("collided with player")            
            for col in self.wall_collide:
                print("collided")
                if self.dir == 1:
                    self.dir = 2
                elif self.dir == 2:
                    self.dir = 1
                elif self.dir == 3:
                    self.dir = 4
                elif self.dir == 4:
                    self.dir = 3
                
            if self.dir == 1:
                self.rect.x -= self.speed
            if self.dir == 2:
                self.rect.x += self.speed
            if self.dir == 3:
                self.rect.y -= self.speed
            if self.dir == 4:
                self.rect.y += self.speed
           """     

                    
        
            
