import pygame

def getMovementControls():
    keys = pygame.key.get_pressed()
    return [keys[pygame.K_t], keys[pygame.K_f],keys[pygame.K_h], keys[pygame.K_SPACE]] #returning up, left, right, and space
