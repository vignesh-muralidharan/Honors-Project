import src
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window_title = "Speedrun"
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# Main game loop
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()        

    #Game Logic
    screen.fill(86)
    # Update the display
    pygame.display.flip()
