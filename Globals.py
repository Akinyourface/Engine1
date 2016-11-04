import pygame
from pygame.locals import *
TILE_WIDTH = 16
TILE_HEIGHT = 16
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class GroupManager:
    all_sprite = pygame.sprite.Group()
    player_sprite = pygame.sprite.Group()
    wall_sprite = pygame.sprite.Group()
    grass_sprite = pygame.sprite.Group()
    enemy_sprite = pygame.sprite.Group()

class Actor(pygame.sprite.Sprite):
    totalActorCount = []
    def __init__(self, x, y, width = TILE_WIDTH, height = TILE_HEIGHT, color = (255, 255, 255), filename = "../Images/default.png", doRender = True):
        super().__init__()
        if doRender == True:
            self.image = pygame.Surface([width, height])
            self.image.fill(color)
            self.imageS = pygame.image.load(filename)
            #self.image.fill(color)
            self.rect = self.image.get_rect()
            self.image.blit(self.imageS, (self.rect.x, self.rect.y))
            self.rect.x = x
            self.rect.y = y   
    def register_subclass(self, name):
        print("Registered " + name +  " as a subclass of Actor") 
        self.totalActorCount.append(name)
    def render(self, display):
        self.image.blit(self.imageS, (self.rect.x, self.rect.y))




        
    


    
