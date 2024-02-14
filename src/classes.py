from src import funcs
import pygame

class Player:
    jumping = False  
    moving = True
    dead = False

    velocity = 10
    direction = 1
    counter = 0


    currentanimation = 'idle'
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
    

    def draw(self, window):
        image = self.animate()
        if self.direction == 1:
            window.blit(image, (self.x,self.y))
        elif self.direction == -1:
            window.blit(pygame.transform.flip(image, True, False), (self.x, self.y))
            
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
        
        if self.dead:
            self.currentanimation = 'dead'

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

    
    def move(self):
        inputs = funcs.movement.getMovementControls()
        if inputs[0] or inputs[3]:
            #jump
            pass
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
