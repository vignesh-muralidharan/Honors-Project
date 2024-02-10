import pygame

def getMovementControls():
    keys = pygame.key.get_pressed()
    return [keys[pygame.K_t], keys[pygame.k_f],keys[pygame.k_h], keys[pygame.K_SPACE]] #returning up, left, right, and space
