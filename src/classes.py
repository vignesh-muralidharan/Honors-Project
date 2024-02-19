from src import funcs
import pygame
import random

class Level:
    numberlimit = random.randint(1,7)
    currentimage = 0
    counter = 0
    def __init__(self, images, surfaces):
        self.images = images
        self.surfaces = surfaces

    def _add_surface_(self, surface):
        self.surfaces.append(surface)
    
    def animate(self, screen):
        if self.counter == self.numberlimit:
            self.counter = 0
            self.numberlimit = random.randint(1,7)
            self.currentimage = 1 if self.currentimage == 0 else 0
        else:
            self.counter += 1
        screen.blit(self.images[self.currentimage], (0,0))
    def check_collisions(self, player):
        #"safe" collisions
        pass
    def update_surfaces(self):
        self.safesurfaces = [i if (i[1] == 1) else None for i in self.surfaces]
        self.safesurfaces = list(filter(None, self.safesurfaces))
        
        self.dangersurfaces = [i if (i[1] == 2) else None for i in self.surfaces]
        self.dangersurfaces = list(filter(None, self.dangersurfaces))

        self.glitchsurfaces = [i if (i[1] == 3) else None for i in self.surfaces]
        self.glitchsurfaces = list(filter(None, self.glitchsurfaces))


class Player:
    jumping = False  
    moving = True
    dead = False
    canjump = False

    stableground = True

    velocity = 10
    direction = 1
    counter = 0
    GRAVITY = 15

    currentanimation = 'fall'
    #animation counter limits

    RUNCL = 23
    DEADCL = 41
    JUMPCL = 34
    IDLECL = 39

    #animation divisors (decides how fast the frames play)
    RUNDIV = 3
    DEADIV = 7
    JUMPDIV = 5
    IDLEDIV = 5

    #ready all assets
    
    #prepare run images
    runimages = funcs.imageuse.getRunImages()

    #prepare jump images
    jumpimages = funcs.imageuse.getJumpImages()

    #prepare dead images
    deadimages = funcs.imageuse.getDeadImages()

    #prepare idle images
    idleimage = funcs.imageuse.getIdleImages()

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x+15, y, 34, 67)

    def draw(self, window):
        image = self.animate()
        if self.direction == 1:
            window.blit(image, (self.x,self.y))
        elif self.direction == -1:
            window.blit(pygame.transform.flip(image, True, False), (self.x, self.y))

        #pygame.draw.rect(window, pygame.color.Color(255,150,0), self.rect, 2)
        self.update()

    def update(self):
        self.rect.x = self.x + 15
        self.rect.y = self.y


    def animate(self):
        #here we update current animation if needed
        #checking for currently idling, if so switch to required animations
        temp = self.currentanimation

    
        if self.currentanimation == 'idle':
            if self.jumping:
                self.currentanimation = 'jump'
            elif self.moving:
                self.currentanimation = 'walk'

        elif self.currentanimation == 'jump':
            if not(self.jumping) and self.moving:
                    self.currentanimation = 'walk'
            elif not(self.jumping) and not(self.moving):
                    self.currentanimation = 'idle'

        elif self.currentanimation == 'walk':
            if self.jumping:
                self.currentanimation = 'jump'
            elif not self.moving:
                self.currentanimation = 'idle'
        elif self.currentanimation == 'fall':
            if self.stableground:
                self.currentanimation = 'idle'


        if self.dead:
            self.currentanimation = 'dead'
        if not(self.stableground):
            self.currnetanimation = 'fall'

        if temp != self.currentanimation:
            self.counter = 0 #reset so animation starts from frame 1
        
        return self.animationhandler()

    def animationhandler(self):
        if self.currentanimation == 'idle':
            if self.counter == self.IDLECL:
                self.counter = 0
            else:
                self.counter += 1

            return self.idleimage[self.counter//self.IDLEDIV]
        
        elif self.currentanimation == 'jump':
            if self.counter == self.JUMPCL:
                self.counter -=  self.JUMPDIV * 2 #to be changed
            else:
                self.counter += 1
            
            return self.jumpimages[self.counter//self.IDLEDIV]
        
        elif self.currentanimation == 'walk':
            if self.counter == self.RUNCL:
                self.counter = 0
            else:
                self.counter += 1
            
            return self.runimages[self.counter//self.RUNDIV]
        
        elif self.currentanimation == 'dead':
            if self.counter == self.DEADCL:
                return True
            else:
                self.counter += 1

            return self.deadimages[self.counter//self.DEADIV]
        
        elif self.currentanimation == 'fall':            
            return self.jumpimages[-2]

    def collide(self, level):
        pass

    def move(self):
        inputs = funcs.movement.getMovementControls()
        if self.stableground:
            if inputs[0] or inputs[3] and self.canjump:
                #jump
                pass
        else:
            #gravity
            self.y += self.GRAVITY
        
        if inputs[1]:
            #left
            self.x -= self.velocity
            self.moving = True
            self.direction = -1

        if inputs[2]:
            #right
            self.x += self.velocity
            self.moving = True
            self.direction = 1

        if inputs[1] and inputs[2]:
            self.moving = False
        if not(inputs[1] or inputs[2]):
            self.moving = False

if __name__ == '__main__':
    print("Compilation Complete")
