import pgzrun
from random import randint

HEIGHT = 600
WIDTH = 1000
c = Actor('chick',(100,100))
w = Actor('walrus',(400,400))
cookie = Actor('cookie', (randint(100,900), randint(100,500)))
score = 0 # variable (global)
speed = 5 # variable (global)

def draw():
    screen.blit('bg', pos=(0,0))
    c.draw()
    w.draw()
    screen.draw.text("A Chicken Story", (10,10), color='red')
    screen.draw.text(f"Score: {score}", (900,10), color='red')
    cookie.draw()

def update():
    global score
    if keyboard.W:
        c.y -= speed
    elif keyboard.S:
        c.y += speed
    elif keyboard.A:
        c.x -= speed
    elif keyboard.D:
        c.x += speed

    if c.colliderect(cookie):
        score +=1
        cookie.pos = (randint(100,900), randint(100,500))
    
pgzrun.go()
