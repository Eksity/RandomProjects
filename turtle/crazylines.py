import turtle as tur
import random
s = tur.getscreen()
a = tur.Turtle()
b = tur.Turtle()
c = tur.Turtle()
d = tur.Turtle()
e = tur.Turtle()
turtles = [a, b, c, d, e]
s.reset()
for t in turtles:
    t.speed(50)
    t.pensize(2)
s.bgcolor("#000000")
i = 0
while True:
    for t in turtles:
        t.color(random.choice(["red", "orange", "green", "blue", "purple"]))
        t.fd(random.randrange(0, 100))
        t.right(random.randrange(0, 360))
        if i >= random.randrange(100, 200):
            t.pu()
            t.home()
            t.pd()
            i = 0
        else:
            i+=1
    