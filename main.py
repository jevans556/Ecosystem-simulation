from ursina import *
from entities import bunny
from entities import food
import random


app = Ursina()
EditorCamera()
bunny_population = []
food_list = []

def GetNumBunnies():
    return wp.content[1].value

def GetFoodAmmount():
    return wp.content[3].value

def StartSimulation():
    num_bunnies = GetNumBunnies()
    num_food = GetFoodAmmount()
    wp.close()

    for x in range(num_bunnies):
        x_pos = random.randrange(-10,10)
        y_pos = random.randrange(-10, 10)
        hunger_drive = random.randrange(1, 10)
        speed = random.randrange(1, 10)
        fertility = random.randrange(1, 10)
        reproductive_urge = random.randrange(1, 10)
        new_bunny = bunny.bunny(x_pos, y_pos, hunger_drive, speed, fertility, reproductive_urge)
        bunny_population.append(new_bunny)

    for x in range(num_food):
        x_pos = random.randrange(-10, 10)
        y_pos = random.randrange(-10, 10)
        new_food = food.food(x_pos, y_pos)
        food_list.append(new_food)
        
wp = WindowPanel(
title='Ecosystem Simulation',
content=(
    Text('Number of Bunnies'),
    Slider(min=1, max=20, default=10, step=1, name='number_of_bunnies'),
    Text('Ammount of Food'),
    Slider(min=0, max=50, default=12, step=1, name='ammount_of_food'),
    Button(text='Start', color=color.azure, on_click=StartSimulation),
    ),
)
wp.y = wp.panel.scale_y / 2 * wp.scale_y

def update():
        
    for bunny in bunny_population:
        bunny.DetermineAction(bunny_population, food_list)
   
app.run()