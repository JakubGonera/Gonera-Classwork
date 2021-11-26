import pygame
import time
import random
import colorsys

class Snowflake:
    def __init__(self) -> None:
        self.x = random.randint(0,700)
        self.y = random.randint(0,500)
        self.speed = 100 * (random.random()/2 + 0.5)
        self.size = random.randint(5,15)
        self.snowColour = [0, 0.5, 1]
    #end procedure
    def update(self, deltaTime):
        self.y += deltaTime * self.speed
        self.snowColour[0] += deltaTime/1000 * self.speed
        if self.y > 500:
            self.y = -15
            self.x = random.randint(0,700)
            self.speed = 100 * (random.random()/2 + 0.5)
            self.size = random.randint(5,15)
        #endif
    #end procedure
    def draw(self, screen):
        self.c = colorsys.hls_to_rgb(self.snowColour[0], self.snowColour[1], self.snowColour[2])
        pygame.draw.rect(screen, (self.c[0] * 255, self.c[1] * 255, self.c[2] * 255), [self.x, self.y, self.size, self.size])
    #end procedure
#end class

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

lastTime = time.time()
snowflakes = []
count = 50
for i in range(0,count):
    snowflakes.append(Snowflake())
#next

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    for i in range(0,count):
        snowflakes[i].update(time.time() - lastTime)
        snowflakes[i].draw(screen)
    #next

    lastTime = time.time()
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()