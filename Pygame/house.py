import pygame
import math
import time

pygame.init()

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0) 

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Window")

done = False
clock = pygame.time.Clock()

sun_x = 0
sun_y = 0
radius = 250

start_time = time.time()

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    screen.fill (BLACK)
    ### SRC - I had an issue with sun_y & sun_x being floats
    sun_y = int(math.sin((time.time() - start_time) / 2 + (3.14 * 3)/4) * radius + 240)
    sun_x = int(math.cos((time.time() - start_time) / 2 + (3.14 * 3)/4) * radius + 320)
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (sun_x,sun_y),40,0)
    pygame.draw.rect(screen, BLACK, (0, 315, 640, 165))

    pygame.display.flip()

    clock.tick(60)
    #End While - End of game loop
pygame.quit()