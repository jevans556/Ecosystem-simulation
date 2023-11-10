from ursina import *
import random

class food(Entity):
    def __init__(self, x_pos, y_pos):
        super().__init__(
            model="cube",
            position=(x_pos, y_pos, 0),
            scale=0.2,
            color=color.orange
        )

    def GetXPosition(self):
        return self.x

    def GetYPosition(self):
        return self.y
        
    def DeleteFood(self):
        self.disable
