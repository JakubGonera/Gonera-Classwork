import pygame
import time
import os

from pygame.constants import K_LEFT, K_RIGHT
from pygame.sprite import DirtySprite

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
base_path = os.path.dirname(__file__)
invader_path = os.path.join(base_path, "invader.png")
player_path = os.path.join(base_path, "player.png")

pygame.font.init() 
font = pygame.font.SysFont('Comic Sans Ms', 50)

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height) -> None:
        super().__init__()
        # Create a sprite
        self.image = pygame.image.load(player_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        # self.image = pygame.Surface([width,height]) 
        # self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = 100
        self.rect.y = 450
    #end procedure
    def update(self, deltaTime):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.rect.x += 5
        #endif
        if keys[K_LEFT]:
            self.rect.x -= 5
        #endif
    #end procedure
    def getXPos(self):
        return self.rect.x
    #end function
#end class

class Bullet(pygame.sprite.Sprite):
    def __init__(self, posX, posY) -> None:
        super().__init__()
        self.image = pygame.Surface([3,8]) 
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
    #end procedure
    def update(self, deltatime):
        self.rect.y -= 6
    #end procedure
    def getYPos(self):
        return self.rect.y
    #end function
#end class

class Enemy(pygame.sprite.Sprite):
    def __init__(self, posX, posY, wave) -> None:
        super().__init__()
        self.image = pygame.image.load(invader_path)
        self.image = pygame.transform.scale(self.image, (30, 30))
        # self.colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        # self.colorImage.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.wave = wave
        self.lastTime = time.time() + 0.1 * wave
        self.stepsMade = 0
        self.direction = True
    #end procedure
    def update(self, deltatime):
        if time.time() - self.lastTime > 1:
            self.lastTime = time.time()
            if self.direction:
                self.rect.x += 10
            else:
                self.rect.x -= 10
            #endif
            self.stepsMade += 1
        if self.stepsMade == 5 and time.time() - self.lastTime > 0.1 * (3 - self.wave):
            self.rect.y += 25
            self.stepsMade = 0
            self.direction = not self.direction
    #end procedure
#end class


pygame.init()
print()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
bullets = []
bulletsGroup = pygame.sprite.Group()

player = Player(GREEN, 20, 20)
spriteGroup = pygame.sprite.Group()
spriteGroup.add(player)

enemiesGroup = pygame.sprite.Group()
enemies = []
waves = 3
for j in range(0, waves):
    for i in range(0, 15):
        enemies.append(Enemy(30 + i * 40, 50 + 50 * j, j))
        spriteGroup.add(enemies[j * 15 + i])
        enemiesGroup.add(enemies[j * 15 + i])
    #next
#next

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
lastTime = time.time()

text = font.render('Game Over', False, WHITE)
isGameOver = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.getXPos() + 10, 450))
                spriteGroup.add(bullets[len(bullets) - 1])
                bulletsGroup.add(bullets[len(bullets) - 1])
            #end if
 
    # --- Game logic should go here
    while bullets and bullets[0].getYPos() < -8:
        bullets[0].kill()
        bullets.pop()
    #end while
    pygame.sprite.groupcollide(enemiesGroup, bulletsGroup, True, True)
    collided = pygame.sprite.spritecollideany(player, enemiesGroup)
    if collided != None:
        for en in enemiesGroup:
            en.kill()
        #next
        player.kill()
        isGameOver = True
    #endif
    spriteGroup.update(time.time() - lastTime)
    lastTime = time.time()

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    spriteGroup.draw(screen)
    
    if isGameOver:
        screen.blit(text, (200, 150))
    #endif

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()