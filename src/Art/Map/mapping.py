import os
import sys
import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 30
temp = []
window_title = "Speedrun"
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
location = "./pain.txt"
for i in range(1,4):
    temp.append(pygame.image.load("./Level{}_Grain.png".format(i)))

current = 0
selectedpoint = None

with open(location, "w") as file:
    file.write("level1 = [")

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit() 
        if keys[pygame.K_l]:
            current += 1
            if current == len(temp):
                current = 0
            with open(location, "a") as file:
                file.write("]\nlevel{} = [".format(current+1))
        if pygame.mouse.get_pressed()[0]:
            selectedpoint = pygame.mouse.get_pos()
        if keys[pygame.K_f]:
            a = "[({},{},{},{}), 1],\n".format(selectedpoint[0], selectedpoint[1], mousepos[0] - selectedpoint[0], mousepos[1] - selectedpoint[1])
            selectedpoint = None
            with open(location, "a") as f1:
                f1.write(a)

        elif keys[pygame.K_d]:
            a = "[({},{},{},{}), 2],\n".format(selectedpoint[0], selectedpoint[1], mousepos[0] - selectedpoint[0], mousepos[1] - selectedpoint[1])            
            selectedpoint = None
            with open(location, "a") as f1:
                f1.write(a)
        
        elif keys[pygame.K_g]:
            a = "[({},{},{},{}), 3],\n".format(selectedpoint[0], selectedpoint[1], mousepos[0] - selectedpoint[0], mousepos[1] - selectedpoint[1])
            selectedpoint = None
            with open(location, "a") as f1:
                f1.write(a)

        if keys[pygame.K_c]:
            selectedpoint = None

    #update display
    screen.blit(temp[current], (0,0))
    if selectedpoint is not None:
        mousepos = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (pygame.color.Color(255,0,0)),pygame.Rect(selectedpoint[0], selectedpoint[1], mousepos[0] - selectedpoint[0], mousepos[1] - selectedpoint[1]), 1)
    
    pygame.display.flip()
    clock.tick(FPS)