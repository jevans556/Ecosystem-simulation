from ursina import *
from entities import bunny
from entities import predator
from entities import food
import random

app = Ursina()
started = False
EditorCamera()
bunny_population = []
food_list = []
predator_population=[]

def GetNumBunnies():
    return wp.content[1].value


def GetNumPredators():
    return wp.content[5].value

def GetFoodAmmount():
    return wp.content[3].value

def StartSimulation():
    index = 0
    global started
    num_bunnies = GetNumBunnies()
    num_food = GetFoodAmmount()
    num_predators = GetNumPredators()
    wp.close()
    started = True

    for x in range(num_bunnies):
        x_pos = random.randrange(-10,10)
        y_pos = random.randrange(-10, 10)
        hunger_drive = random.randrange(1, 10)
        speed = random.randrange(1, 10)
        fertility = random.randrange(1, 10)
        reproductive_urge = random.randrange(1, 10)
        new_bunny = bunny.bunny(index, x_pos, y_pos, hunger_drive, speed, fertility, reproductive_urge)
        bunny_population.append(new_bunny)
        index += 1

    for x in range(num_predators):
        x_pos = random.randrange(-10, 10)
        y_pos = random.randrange(-10, 10)
        hunger_drive = random.randrange(1, 10)
        speed = random.randrange(1, 10)
        new_predator = predator.predator(
            x_pos, y_pos, hunger_drive, 10)
        predator_population.append(new_predator)

    for x in range(num_food):
        x_pos = random.randrange(-50, 50)
        z_pos = random.randrange(-50, 50)
        new_food = food.food(x_pos, z_pos)
        food_list.append(new_food)
        
wp = WindowPanel(
title='Ecosystem Simulation',
content=(
    Text('Number of Bunnies'),
    Slider(min=1, max=20, default=10, step=1, name='number_of_bunnies'),
    Text('Ammount of Food'),
    Slider(min=0, max=50, default=12, step=1, name='ammount_of_food'),
    Text('Number of predators'),
    Slider(min=0, max=10, default=3, step=1, name='number_of_predators'),
    Button(text='Start', color=color.azure, on_click=StartSimulation),
    ),
)
wp.y = wp.panel.scale_y / 2 * wp.scale_y

def update():
    end_simulation = True
    for bunny in bunny_population:
        bunny.DetermineAction(bunny_population, food_list)
        if bunny.enabled == True:
            end_simulation = False

    for predator in predator_population:
        predator.DetermineAction(predator_population, bunny_population)
        if predator.enabled == True:
            end_simulation = False

    if end_simulation and started:
        text = Text(text="All Bunnies Have Died :(", x=-0.5, y=0, color=color.red, scale = 3)
   
app.run()