from ursina import *
import random
import math

class bunny(Entity):
    def __init__(self, x_pos, y_pos, hunger_drive, speed, fertility, reproductive_urge):
        super().__init__(
            #define Entity parameters here. Entity parameters can then be accessed with self.<Entity Parameter>
            model="models/dragon.obj",
            position=(x_pos, y_pos, 0),
            scale = 0.25
        )
        self.rand_x = random.randrange(-50, 50)
        self.rand_y = random.randrange(-50, 50)
        self.rand_z = random.randrange(-50, 50)
        self.hunger_drive = hunger_drive # scale value used to determine how fast a bunny will get hungry
        self.hunger_threshhold = 30 # threshold used to determine when bunny will start looking for food
        self.target_position = Vec3(self.rand_x, self.rand_y, self.rand_z)
        self.at_current_target = False
        self.hunger_level = 100
        self.speed = speed
        self.fertility = fertility # used to determine how many offspring a bunny will produce
        self.reproductive_urge = reproductive_urge #scale value used to determine how fast a bunny will start looking for a mate
        self.reproductive_threshold = 30 # threshold used to determine when bunny will start looking for mate
        self.horniness_level = 100
        self.looking_for_mate = False #bunnies will only reproduce with other bunnies who's looking for mate flag is set to True
        #need to fix bug related to text generation. Text needs to be above bunny's head
        self.text = Text(text="test", x=self.x, y=self.scale_y * 2, parent=self, color=color.red)

    def DetermineAction(self, bunny_population, food=None):
        #TODO main loop for determining next bunny action. Should probably be called in main game loop
        #need to update hunger and reproductive urge levels and check to see if they are below the specified
        #threshold. If either are below the threshold, then make the bunny find food/available mate and update
        #levels accordingly. Use the target position parameter to make the bunny move to particular location
        self.MoveToLocation(self.target_position, self.speed)
        self.text.position = (self.scale_x, self.scale_y + 2)

        if self.at_current_target:
            self.at_current_target = False
            self.GenerateRandomLocation()
            self.MoveToLocation(self.target_position, 3)

    def GenerateRandomLocation(self):
        self.rand_x = random.randrange(-50, 50)
        self.rand_y = random.randrange(-50, 50)
        self.rand_z = random.randrange(-50, 50)
        self.target_position = Vec3(self.rand_x, self.rand_y, self.rand_z)
        
    def MoveToLocation(self, target, speed):
        self.look_at(target)
        direction_vector = target - self.position
        distance = direction_vector.length()
        direction_vector.normalize()
        self.position += direction_vector * speed * time.dt

        if distance < speed * time.dt:
            self.position = target
            self.at_current_target = True

    def RotateBunny(self, rotation_y, rotation_x):
        self.rotation_y = self.rotation_y + rotation_y
        self.rotation_x = self.rotation_x + rotation_x

    def UpdateHungerLevel():
        #TODO logic to update hunger level
        pass

    def FindFood(self):
        #TODO logic to find food goes here
        pass

    def UpdateReproductiveUrge():
        #TODO logic to update bunny lust
        pass

    def FindMate(self):
        #TODO program NSFW bunny desires here
        pass
    def DespawnBunny(self):
        self.disable()

    def ProduceOffspring(self, bunny_population):
        #TODO logic for producing more bunnies
        pass

    def AddText(self, text):
        #TODO fix bug related to adding text above the bunnies
        self.text.y = self.scale_y * 2
        self.text.text = text

    def BunnyToStr(self):
        print(f"x_pos:{self.x_pos} y_pos:{self.y_pos} scale:{self.scale} speed:{self.speed} fertility:{self.fertility} reproductive_urge:{self.reproductive_urge}")