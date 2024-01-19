import os
import sys
import pygame
#important information::
"""Run1 -- up:1, down:0, left:0, right:0
Run2 -- up:1, down:0, left:7, right:3
Run3 -- up:-1, down:0, left:15, right:3
Run4 -- up:2, down:0, left:23, right:0
Run5 -- up:2, down:0, left:6, right:3
Run6 -- up:1, down:0, left:-6, right:1
Run7 -- up:-1, down:0, left:3, right:0
Run8 -- 0, 0, 1, 0"""
pygame.init()
counter = 0
window_title = "Speedrun"
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)


images = [pygame.image.load("./Run/{}".format(path)) for path in os.listdir("./Run")]
runoffset = [0,3,3,0,3,1,0,0]
for i in images:
    i.convert_alpha()

# Main game loop
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()        

    #Game Logic
    screen.fill((255,255,255))
    screen.blit(images[counter//30], (100-runoffset[counter//30],100))
    if counter == 230:
        counter = 0
    else:
        counter+=1

    # Update the display
    pygame.display.flip()

