import src
import pygame
import sys

# Initialize Pygame
pygame.init()

#limit FPS
FPS = 30
clock = pygame.time.Clock()

# Set up the window
window_title = "Speedrun"
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

Player = src.classes.Player(100,100)

# Main game loop
while True:
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()        

    #Game Logic
    screen.fill((255,255,255))
    # Update the display
    Player.draw(screen)
    Player.move()

    
    pygame.display.flip()
    clock.tick(FPS)
