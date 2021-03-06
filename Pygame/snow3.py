import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
class House(pygame.sprite.Sprite): 
# Define the constructor for house 
  def __init__(self, color, width, height): 
  # Call the sprite constructor
    super().__init__() 
    # Create a sprite and fill it with colour 
    self.image = pygame.Surface([width,height]) 
    self.image.fill(color) 
    # Set the position of the sprite 
    self.rect = self.image.get_rect() 
    self.rect.x = 100 
    self.rect.y = 450 
  #End Procedure
#End Class


## -- Define the class snow which is a sprite 
class Snow(pygame.sprite.Sprite): 
# Define the constructor for snow 
  def __init__(self, color, width, height): 
  # Call the sprite constructor 
    super().__init__() 
    # Create a sprite and fill it with colour 
    self.image = pygame.Surface([width,height]) 
    self.image.fill(color) 
    # Set the position of the sprite 
    self.rect = self.image.get_rect() 
    self.rect.x = random.randrange(0, 700) 
    self.rect.y = random.randrange(0, 400) 
    self.speed = random.randrange(1, 4)
  #End Procedure
  def update(self):
      self.rect.y += self.speed
      if self.rect.y > 500:
          self.rect.y = -10
        #endif
    #end procedure
#End Class

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
sprites = []
snow_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
sprites.append(House(RED, 100, 50))
all_sprites_group.add(sprites[0])
for n in range(50):
  sprites.append(Snow(WHITE,10,10))
  all_sprites_group.add(sprites[n])
  snow_group.add(sprites[n])
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    all_sprites_group.update()
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    all_sprites_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()