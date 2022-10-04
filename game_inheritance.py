from random import randint as ri
import pgzrun

WIDTH = 640
HEIGHT = 480

# all the class logic
class Player(Actor):    
    # override the default contructor
    def __init__(self, image, speed=5): 
        pos = ri(0, WIDTH), ri(0, HEIGHT)  # generate a random x,y coordinte
        super().__init__(image, pos) # call the parent class constructor and pass image and pos
        self.speed = speed  # add a new instance variable
        
    def move(self):
        if keyboard.W:
            self.y -= self.speed
        elif keyboard.S:
            self.y += self.speed
        elif keyboard.A:
            self.x -= self.speed
            self.angle = +10
        elif keyboard.D:
            self.x += self.speed
            self.angle = -10
        else:
            self.angle = 0

    def check_boundary(self):
        if self.x < 0: # agar player left side se bahar ja raha h
            self.x = WIDTH # to right side pe dikhne lage
        if self.x > WIDTH: # vice versa
            self.x = 0 
        if self.y < 0:
            self.y = HEIGHT
        if self.y > HEIGHT:
            self.y = 0

# main game code
p = Player('ironman', 3)
def draw():
    screen.fill('black')
    screen.blit('bg', (0, 0))
    p.draw()
def update():
    p.move()
    p.check_boundary()
pgzrun.go()