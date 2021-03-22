from robot_class import Robot
from weapon_class import Weapon



class Fleet:
    def __init__(self):
        self.my_robot1 = Robot(Weapon)
        self.my_robot2 = Robot(Weapon)
        self.my_robot3 = Robot(Weapon)