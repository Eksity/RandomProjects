import turtle as tur
import random
s = tur.getscreen()
t = tur.Turtle()
s.reset()
t.speed(10)
t.pensize(2)
while True:
    t.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
    t.pu()
    t.home()
    t.pd()
    t.goto(random.randrange(-500, 500), random.randrange(-500, 500))
    