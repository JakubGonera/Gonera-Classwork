### SRC - Good code.
import pygame
import math
import time

from pygame.constants import K_DOWN, KEYDOWN

pygame.init()

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0) 

WIDTH = 640
HEIGHT = 480

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

done = False
clock = pygame.time.Clock()

ball_width = 20
x_val = 150
y_val = 200

x_direction = 1
y_direction = 1

padd_length = 60
padd_width = 15

x_padd = 0
y_padd = 20

start_time = time.time()

while not done:
    # -- User input and controls

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y_padd -= 5
    if keys[pygame.K_DOWN]:
        y_padd += 5

    y_padd = max(0, y_padd)
    y_padd = min(HEIGHT - padd_length, y_padd)

    screen.fill (BLACK)

    x_val = x_val + x_direction
    y_val = y_val + y_direction

    if x_val == padd_width and y_val >= y_padd and y_val <= y_padd + padd_length:
        x_direction *= -1
    #End if
    if x_val < 0:
        x_val = 150
        y_val = 200
        x_direction = 1
        y_direction = 1
    #End if
    if x_val == WIDTH - ball_width:
        x_direction *= -1
    #End if
    if y_val == 0 or y_val == HEIGHT - ball_width:
        y_direction *= -1
    #End if

    pygame.draw.rect(screen, BLUE, (x_val,y_val,20,20))
    pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_width, padd_length))

    pygame.display.flip()

    clock.tick(60)
    #End While - End of game loop
pygame.quit()