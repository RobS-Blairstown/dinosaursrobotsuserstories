from weapon_class import Weapon


class Robot:
    def __init__(self):
        self.name = 'MK-177'
        self.health = '200'
        self.power_level = '75'
        self.weapon = Weapon
        self.attack_power = '10'

    def robot_weapon_choice(self):
        response = input('Which type of weapon do you want to use? Katana, Mace or Ka-Bar?')
        self.weapon = response
