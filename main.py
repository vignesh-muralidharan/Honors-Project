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

levels = [src.classes.Level(src.src.funcs.imageuse.getLevelImages(i), []) for i in range(1,4)]
levelhitboxes = [src.hitboxdata.level1, src.hitboxdata.level2, src.hitboxdata.level3]
for i in range(0,3):
    for j in levelhitboxes[i]:
        levels[i]._add_surface_(j)
    levels[i].update_surfaces()
currentlevel = 0

# Main game loop
while True:
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()     
        if keys[pygame.K_l]:
            currentlevel += 1
            if currentlevel == len(levels):
                currentlevel = 0    

    #Game Logic
    # Update the display
    levels[currentlevel].animate(screen)
    Player.draw(screen)
    Player.move()
    
    
    pygame.display.flip()
    clock.tick(FPS)
