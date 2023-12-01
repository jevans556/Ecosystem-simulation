from ursina import *
import random

class food(Entity):
    def __init__(self, x_pos, z_pos):
        super().__init__(
            model="models/carrot.obj",
            position=(x_pos, 0.5, z_pos),
            scale=1.5,
            texture="textures/carrot_textures/Carrot_Texture.png",
            color=color.orange
        )

    def GetXPosition(self):
        return self.x

    def GetYPosition(self):
        return self.y

    def GetZPosition(self):
        return self.z
        
    def DeleteFood(self):
        self.disable()
