import pygame
import os

pygame.display.set_mode((0,0))
def getRunImages():
    temp = [pygame.image.load("./src/Art/Run/{}".format(path)) for path in os.listdir("./src/Art/Run")]
    [i.convert_alpha() for i in temp]
    return temp

def getJumpImages():
    temp = [pygame.image.load("./src/Art/Jump/{}".format(path)) for path in os.listdir("./src/Art/Jump")]
    [i.convert_alpha() for i in temp]
    return temp

def getDeadImages():
    temp = [pygame.image.load("./src/Art/Dead/{}".format(path)) for path in os.listdir("./src/Art/Dead")]
    [i.convert_alpha() for i in temp]
    temp.append(temp[-1])  #extending dead frame further , first length is 4, now length becomes 6
    temp.append(temp[-1])
    return temp

def getIdleImages():
    temp = [pygame.image.load("./src/Art/Idle/{}".format(path)) for path in os.listdir("./src/Art/Idle")]
    [i.convert_alpha() for i in temp]
    return temp

