import pygame
import sys
from random import randrange
import time

# Initialize Pygame modules
pygame.init()

# Set Display
surface = pygame.display.set_mode(size=(750, 500))

# Hide the mouse so its just a dot
pygame.mouse.set_visible(False)

test = 0
timer = time.time()
xpos = 0
ypos = 0


# Main Body Of Program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    mouse = pygame.mouse.get_pos()
    surface.fill((0,0,0))
    pygame.draw.circle(surface, (255,255,255), mouse, 5)

    text = pygame.font.Font(None, 20)
    text.render("Hello", True, [200,200,0])

    # Display target
    if time.time() < timer + 2:
        pygame.draw.circle(surface, (255,0,0), (xpos, ypos), 5)
    else: 
        timer = time.time()
        xpos = randrange(50, 700)
        ypos = randrange(50, 450)

    if mouse[0] < xpos + 2 and mouse[0] > xpos - 2 and mouse[1] < ypos + 2 and mouse[1] > ypos - 2:
        test = test + 1
        timer = time.time()
        xpos = randrange(50, 700)
        ypos = randrange(50, 450)
        print(test)
    # Add else statement for when you miss

    # Update display
    pygame.display.update()

