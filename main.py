import pygame

# Initialize pygame
pygame.init()

# Create the screen
# Provide the height and width as arguments
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RGB - Red, Green, Blue
    screen.fill((255, 0, 0))
    pygame.display.update()



        


