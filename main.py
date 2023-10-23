from ursina import *

app = Ursina()

definitely_a_rabbit = Entity(model="models/dragon.obj", scale=0.25)
EditorCamera()

def update():
    definitely_a_rabbit.rotation_y = definitely_a_rabbit.rotation_y + 0.25


app.run()