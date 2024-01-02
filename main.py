import src
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
window_title = "Speedrun"
window_size = (width, height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Add your game logic or drawing code here

    # Update the display
    pygame.display.flip()
