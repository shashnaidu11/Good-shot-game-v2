#importing the libraries
import random
import pgzrun

TITLE="good shot game"
WIDTH=600
HEIGHT=600

msg=""

#Creating the charector
alien=Actor("alien")

def draw():
    screen.clear()
    screen.fill(color=("Red"))
    alien.draw()
    screen.draw.text(msg,center=(300,20),fontsize=30)

def move_alien():
    alien.x=random.randint(50,550)
    alien.y=random.randint(50,550)


def on_mouse_down(pos):
    global msg
    if alien.collidepoint(pos):
        move_alien()
        msg= "Good Shot"
    else:
        msg="You missed"
move_alien()        











pgzrun.go()