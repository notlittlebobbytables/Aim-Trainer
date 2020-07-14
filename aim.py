import pygame
import sys
from random import randrange
import time

# Initialize Pygame modules
pygame.init()

# Set Display
surface = pygame.display.set_mode(size=(1920//2, 1080//2))

text = pygame.font.SysFont("Comic Sans MS", 30)

# Also Works
# text = pygame.font.Font(None, 30)

# Hide the mouse so its just a dot
pygame.mouse.set_visible(False)

test = 0
timer = time.time()
xpos = randrange(50, 700)
ypos = randrange(50, 450)
score = 0


# Main Body Of Program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Checks to see if target was hit or not
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0] < xpos + 4 and mouse[0] > xpos - 4 and mouse[1] < ypos + 4 and mouse[1] > ypos - 4:
                score += 1
                timer = time.time()
                xpos = randrange(50, 700)
                ypos = randrange(50, 450)
        
    # Add else statement for when you miss??
    
    mouse = pygame.mouse.get_pos()
    surface.fill((0,0,0))
    pygame.draw.circle(surface, (255,255,255), mouse, 5)

    # Display target
    if time.time() < timer + 2:
        pygame.draw.circle(surface, (255,0,0), (xpos, ypos), 5)
    else: 
        timer = time.time()
        xpos = randrange(50, 700)
        ypos = randrange(50, 450)

    surface.blit(text.render(f"Score: {score}", True, (255,255,255)), (0,0))

    # Update display
    pygame.display.update()

