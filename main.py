from ursina import *
from entities import bunny
import random

app = Ursina()
EditorCamera()
num_bunnies = 8
bunny_population = []

for x in range(num_bunnies):
    x_pos = random.randrange(-10,10)
    y_pos = random.randrange(-10, 10)
    hunger_drive = random.randrange(0, 10)
    speed = random.randrange(0, 10)
    fertility = random.randrange(0, 10)
    reproductive_urge = random.randrange(0, 10)
    new_bunny = bunny.bunny(x_pos, y_pos, hunger_drive, speed, fertility, reproductive_urge)
    bunny_population.append(new_bunny)

def update():

    for bunny in bunny_population:
        bunny.DetermineAction(bunny_population)

app.run()