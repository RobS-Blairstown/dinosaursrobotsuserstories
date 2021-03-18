

class Weapon:
    def __init__(self):
        self.weapon_type = ''
        self.weapon_power = ''
        self.weapon_speed = ''

    def katana(self):
        self.weapon_type = 'Sword'
        self.weapon_power = '35'
        self.weapon_speed = 'Medium'

    def mace(self):
        self.weapon_type = 'Club'
        self.weapon_power = '50'
        self.weapon_speed = 'Slow'

    def ka_bar(self):
        self.weapon_type = 'Dagger'
        self.weapon_power = '20'
        self.weapon_speed = 'Fast'


