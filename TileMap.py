from Globals import *
from Grass import *
from Wall import *
from Enemy_follow import *
from EnemyRotate import *
class TileMap:
    def __init__(self, filename = "default.txt"):
        self.filename = filename 
        self.level = [row.strip('\n') for row in open("../Levels/level1.txt", 'r').readlines()]
        
        self.levelWidth = len(self.level[0])
        self.levelHeight = len(self.level)
        #self.rect = pygame.Rect((self.levelWidth, self.levelHeight))
        self.blockWidth = 16
        self.localCamX = 0
        self.localCamY = 0
    def reload_map(self):
        self.level = [row.strip('n') for row in open(self.filename, 'r').readlines()]
    def draw_map(self, display):
        for x in range(self.levelWidth):
            for y in range(self.levelHeight):
                if self.level[y][x] == "0":
                    #print("it works")
                    wall = Wall(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.wall_sprite.add(wall)
                    GroupManager.all_sprite.add(wall)
                if self.level[y][x] == ".":
                    grass = Grass(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.grass_sprite.add(grass)
                    #GroupManager.all_sprite.add(grass)
                if self.level[y][x] == "1":
                    enemy = Enemyfollow(x * self.blockWidth, y * self.blockWidth)
                    enemy.walls = GroupManager.wall_sprite
                    enemy.player = GroupManager.player_sprite
                    GroupManager.enemy_sprite.add(enemy)
                if self.level[y][x] == "2":
                    enemy = EnemyRotate(x * self.blockWidth, y * self.blockWidth)
                    GroupManager.enemy_sprite.add(enemy)
