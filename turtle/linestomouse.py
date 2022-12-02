import turtle as tur
import random
canvas = tur.getcanvas()
t = tur.Turtle()
x, y = canvas.winfo_pointerxy()
while True:
    t.color(random.choice(["red", "orange", "green", "blue", "purple"]))
    print(x, y)

