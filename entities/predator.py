from ursina import *
import random
import math


class predator(Entity):
    def __init__(self, x_pos, z_pos, hunger_drive, speed):
        super().__init__(
            # define Entity parameters here. Entity parameters can then be accessed with self.<Entity Parameter>
            model="models/fox.obj",
            texture="textures/fox_textures/texture.png",
            position=(x_pos, 0, z_pos),
            scale=0.08
        )
        self.rand_x = random.randrange(-50, 50)
        self.rand_y = random.randrange(-50, 50)
        self.rand_z = random.randrange(-50, 50)
        # scale value used to determine how fast a bunny will get hungry
        self.hunger_drive = hunger_drive
        # threshold used to determine when bunny will start looking for food
        self.hunger_threshhold = 60
        self.looking_for_food = False
        self.target_position = Vec3(self.rand_x, 0, self.rand_z)
        self.at_current_target = False
        self.hunger_level = 100
        self.speed = speed
        

    def DetermineAction(self, bunny_population, food=None):
        self.UpdateHungerLevel(food)

        if self.hunger_level < self.hunger_threshhold:
            self.looking_for_food = True
            food_index = self.FindFood(food)


        self.MoveToLocation(self.target_position, self.speed)

        if self.at_current_target:
            if self.looking_for_food:
                if food:
                    food[food_index].DespawnBunny(food)
                    self.hunger_level = 100
                    self.looking_for_food = False

            self.at_current_target = False
            self.GenerateRandomLocation()
            self.MoveToLocation(self.target_position, 3)

    def GenerateRandomLocation(self):
        self.rand_x = random.randrange(-50, 50)
        self.rand_z = random.randrange(-50, 50)
        self.target_position = Vec3(self.rand_x, 0, self.rand_z)

    def MoveToLocation(self, target, speed):
        self.look_at(target)
        direction_vector = target - self.position
        origin = self.world_position + (self.up*.5)
        hit_info = raycast(origin, direction_vector, ignore=(
            self,), distance=.7, debug=False)
        distance = direction_vector.length()
        direction_vector.normalize()

        if not hit_info.hit:
            self.position += direction_vector * speed * time.dt

        else:
            self.GenerateRandomLocation()

        if distance < speed * time.dt:
            self.position = target
            self.at_current_target = True

    def RotateBunny(self, rotation_y, rotation_x):
        self.rotation_y = self.rotation_y + rotation_y
        self.rotation_x = self.rotation_x + rotation_x

    def UpdateHungerLevel(self,list):
        if self.hunger_level < 0:
            self.DespawnBunny()
            return
        hunger_multplier=.01
        if len(list)>100 :
            self.hunger_level=50
        self.hunger_level -= self.hunger_drive * hunger_multplier

    def FindFood(self, food):
        nearest_distance = Vec3(100000, 100000, 100000)
        self.at_current_target = False
        food_index = None
        if food == None:
            self.GenerateRandomLocation()
            return

        for i, food in enumerate(food):
            current_distance = Vec3(self.position - food.position).length()
            if current_distance < nearest_distance:
                nearest_distance = current_distance
                self.target_position = food.position
                food_index = i

        return food_index


    def DespawnBunny(self):
        self.disable()

    def BunnyToStr(self):
        print(f"x_pos:{self.x_pos} y_pos:{self.y_pos} scale:{self.scale} speed:{self.speed} ")
