import os
import sys
import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 30
counter = 0
runcounter = 0
deadcounter = 0
jumpcounter = 0

window_title = "Speedrun"
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

#prepare run images
runimages = [pygame.image.load("./src/Art/Run/{}".format(path)) for path in os.listdir("./src/Art/Run")]
[i.convert_alpha() for i in runimages]

#prepare jump images
jumpimages = [pygame.image.load("./src/Art/Jump/{}".format(path)) for path in os.listdir("./src/Art/Jump")]

#prepare dead images
deadimages = [pygame.image.load("./src/Art/Dead/{}".format(path)) for path in os.listdir("./src/Art/Dead")]
[i.convert_alpha() for i in deadimages]
deadimages.append(deadimages[-1])  #extending dead frame further , first length is 4, now length becomes 6
deadimages.append(deadimages[-1])

#prepare idle images
idleimage = [pygame.image.load("./src/Art/Idle/{}".format(path)) for path in os.listdir("./src/Art/Idle")]
idleimage[0].convert_alpha()

# Main game loop
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()        

    #Game Logic
    #Drawing Running Character
    screen.fill((255,255,255))
    screen.blit(runimages[runcounter//3], (100,100))
    #Drawing Dying Character
    screen.blit(deadimages[deadcounter//7], (200,100))
    #Drawing Jumping Character
    screen.blit(jumpimages[jumpcounter//5], (300,100))
    #Drawing Idle Image
    screen.blit(idleimage[0], (400,100))

    #updating counters
    if deadcounter == 41:
        deadcounter = 0
    else:
        deadcounter+= 1
    #---------
    if runcounter == 23:
        runcounter = 0
    else:
        runcounter+=1
    #----------
    if jumpcounter == 34:
        jumpcounter = 0
    else:
        jumpcounter += 1
    


    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

