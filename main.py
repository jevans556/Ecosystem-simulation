from ursina import *
from entities import bunny
from entities import food
import random

app = Ursina()
EditorCamera()
num_bunnies = 8
num_food = 10
bunny_population = []
food_list = []

for x in range(num_bunnies):
    x_pos = random.randrange(-10,10)
    y_pos = random.randrange(-10, 10)
    hunger_drive = random.randrange(0, 10)
    speed = random.randrange(0, 10)
    fertility = random.randrange(0, 10)
    reproductive_urge = random.randrange(0, 10)
    new_bunny = bunny.bunny(x_pos, y_pos, hunger_drive, speed, fertility, reproductive_urge)
    bunny_population.append(new_bunny)

for x in range(num_food):
    x_pos = random.randrange(-10, 10)
    y_pos = random.randrange(-10, 10)
    new_food = food.food(x_pos, y_pos)
    food_list.append(new_food)

def update():

    for bunny in bunny_population:
        bunny.DetermineAction(bunny_population, food_list)

app.run()