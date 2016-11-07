from Globals import *



class Player(Actor):
    def __init__(self, startingx, startingy):
        super().__init__(startingx, startingy, TILE_WIDTH, TILE_HEIGHT, (0, 0, 0), "../Images/player.png")
        self.dir = 0
        super().register_subclass("player")
        self.deltax = 0
        self.deltay = 0
        self.image.set_colorkey((255, 0, 255))
        self.playerspeed = 2
    def _update_keypressed(self, event):
        
        if event.key == pygame.K_a:
            #player.dir = 1
            self.deltax = -10
        if event.key == pygame.K_d:
            #player.dir = 2
            self.deltax = 10
        if event.key == pygame.K_w:
            #player.dir = 3
            self.deltay = -10
        if event.key == pygame.K_s:
            #player.dir = 4
            self.deltay = 10
        
            
    def _update_keyup(self, event):
        
        if event.key == pygame.K_a:
            self.deltax = 0 
        if event.key == pygame.K_d:
            self.deltax = 0
        if event.key == pygame.K_w:
            self.deltay = 0
        if event.key == pygame.K_s:
            self.deltay = 0

    def update(self):
       #super().actor_update()
        #self.image = pygame.transform.scale(self.image, (self.rect.width * Camera.CameraZoom, self.rect.height * Camera.CameraZoom))
        #self.rect = self.image.get_rect()    
        self.rect.x += self.deltax
        self.block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        self.rect.y += self.deltay
        for block in self.block_hit_list:
            if self.deltax > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        self.block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in self.block_hit_list:
            if self.deltay > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
