

class Dinosaur:
    def __init__(self, type, health, energy, attack_power):
        self.type = type
        self.health = health
        self.energy = energy
        self.attack_power = attack_power


    def t_rex_type(self):
        self.type = "T-Rex"
        self.health = '80'
        self.energy = '50'
        self.attack_power = '95'

    def velociraptor_type(self):
        self.type = "Velociraptor"
        self.health = '50'
        self.energy = '120'
        self.attack_power = '60'

    def stegosaurus_type(self:
        self.type = "Stegosaurus"
        self.health = '120'
        self.energy = '60'
        self.attack_power = '75'
