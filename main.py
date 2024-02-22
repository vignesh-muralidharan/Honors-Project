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

for i in range(0,3):
    levels[i].playerstart = src.hitboxdata.start[i]
    levels[i].winrect = pygame.Rect(src.hitboxdata.winrects[i])
    for j in src.hitboxdata.levelhitboxes[i]:
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
    _ = Player.draw(screen)
    if _ == 'dead':
        levels[currentlevel].reset(Player)
        Player.dead = False
        Player.counter = 0
        Player.currentanimation = 'idle'
        _ = 'restart'
        continue

    __ = Player.move(levels[currentlevel])
    if __ == "next":
        currentlevel += 1
        __ = 'stay'
        if currentlevel == len(levels):
                currentlevel = 0
                Player.x,Player.y = (0,100) 
    Player.collide(levels[currentlevel])
    

    #debugtime
    font = pygame.font.SysFont("Arial", 30)
    text = font.render("CanJump: {}, Jumping: {}, Stableground: {}, Jumpcounter: {} ".format(Player.canjump, Player.jumping, Player.stableground, Player.jumpcounter), True, (0,0,0))
    screen.blit(text, (0,0))
    
    #debug code::
    #pygame.draw.rect(screen, (255,130,130), levels[currentlevel].winrect, 1)
    levels[currentlevel].debug(screen)
    #refresh display
    pygame.display.flip()
    clock.tick(FPS)
