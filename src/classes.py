from src import funcs

class Player:
    jumping = False  
    moving = False
    direction = 1
    counter = 0

    #animation counter limits
    runcl = 23
    deadcl = 41
    jumpcl = 34

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
        #image = self.animate()
        image = self.idleimage[0]
        window.blit(image, (self.x,self.y))

    def animate(self):
        #return current state of animation // animation handler decides which image to use currently, and whether a change needs to be made
        pass

    def animationhandler(self):
        pass
        

    def move(self):
        inputs = funcs.movement.getMovementControls()
        if inputs[0] or inputs[3]:
            #jump
            pass
        if inputs[1]:
            #left
            self.x -= 5
        if inputs[2]:
            #right
            self.x += 5

if __name__ == '__main__':
    print("Compilation Complete")
