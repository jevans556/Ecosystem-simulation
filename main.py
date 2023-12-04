from ursina import *
from entities import bunny
from entities import predator
from entities import food
import random
from ursina.shaders import lit_with_shadows_shader


class Lights:
    def __init__(self):
        self.pivot = Entity()
        self.direc_light = DirectionalLight(
            parent=self.pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))
        self.amb_light = AmbientLight(
            parent=self.pivot, color=color.rgba(100, 100, 100, 0.1))

app = Ursina()
Entity.default_shader = lit_with_shadows_shader

Lights()
pivot = Lights().pivot
direc_light = Lights().direc_light
amb_light = Lights().amb_light

started = False
Sky()

camera = EditorCamera(orthographic=True)
camera.rotation_x = 90  # Set the rotation to achieve top-down view
camera.position = (0, 30, 0)  # Adjust the height as needed

terrain = Entity(model='plane', scale=(105, 1, 105), texture= 'textures/Grass2.jpg')

# Make sure to set the model for lakes and forests
big_lake = Entity(model='cube', collider='box', scale=(30, 1, 30), position=(-20, 0, 29), texture='textures/water.jpeg')
small_lake1 = Entity(model='cube', collider='box', scale=(9, 1, 9), position=(-25, 0, -10), texture='textures/water.jpeg')
small_lake2 = Entity(model='cube', collider='box', scale=(11, 1, 11), position=(5, 0, -30), texture='textures/water.jpeg')
small_lake3 = Entity(model='cube', collider='box', scale=(14, 1, 9), position=(26, 0, 0), texture='textures/water.jpeg')


dark_green = color.rgb(0, 0.5, 0)
def create_forest(x1, x2, y1, y2):
    x_pos = random.uniform(x1, x2)  # Adjust the x-axis range
    z_pos = random.uniform(y1, y2)  # Adjust the z-axis range
    return Entity(model='cube', scale=(6, 1, 6), position=(x_pos, 0, z_pos), texture='textures/bushtree.png')

# Create a forest with a random cluster of trees

#Forest 1
for _ in range(17):
    create_forest(17, 35, 24, 35)
for _ in range(5):
    create_forest(20, 35, 24, 30)

#Forest 2
for _ in range(6):
    create_forest(-10, 0, 2, 8)

#Forest 3
for _ in range(8):
    create_forest(-27, -40, -30, -35)

#Forest 4
for _ in range(14):
    create_forest(20, 30, -20, -30)

#Scatered trees
for _ in range(6):
    create_forest(-47, 47, -47, 47)

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
        speed = random.randrange(3, 20)
        fertility = random.randrange(1, 5)
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
            x_pos, y_pos, hunger_drive, 25)
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

    if end_simulation and started:
        text = Text(text="All Bunnies Have Died :(", x=-0.5, y=0, color=color.red, scale = 3)
   
app.run()