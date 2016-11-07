from Globals import *
from Player import *
from Camera import *
from TileMap import *



class Engine:
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    isRunning = True
    player = Player(10, 10)
    tm = TileMap()
    
    
    clock = pygame.time.Clock()
    GroupManager.player_sprite.add(player)
    background = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
    background.fill([0, 0, 0])
    background.set_colorkey((255, 0, 255))
    
    
    
    GroupManager.all_sprite.add(player)
    
    tm.draw_map(display)
    
    player.walls = GroupManager.wall_sprite
    @staticmethod
    def update():
        pygame.init()
        while Engine.isRunning:
            #game loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    Engine.player._update_keypressed(event)
                    if event.key == pygame.K_ESCAPE:
                        Engine.isRunning = False
                if event.type == pygame.KEYUP:
                    Engine.player._update_keyup(event)
                if event.type == pygame.QUIT:
                    Engine.isRunning = False
            Engine.display.fill([255, 255, 255])
            for ent in GroupManager.enemy_sprite:
                ent._update(Engine.player)
            Camera.Camera_Transform(Engine.player, Engine.isRunning)
            GroupManager.all_sprite.update()
            Engine.display.blit(Engine.background, (0, 0))
            
            GroupManager.grass_sprite.draw(Engine.display)
            GroupManager.all_sprite.draw(Engine.display)
            GroupManager.enemy_sprite.draw(Engine.display)
            pygame.display.update()
            Engine.clock.tick(60)
        pygame.quit()


