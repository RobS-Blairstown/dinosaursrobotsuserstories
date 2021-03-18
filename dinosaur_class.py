

class Dinosaur:
    def __init__(self):
        self.type = ''
        self.health = ''
        self.energy = ''
        self.attack_power = ''

    def dinosaur_type(self):
        response = input('What type of dinosaur do you want? T-Rex, Velociraptor or Stegosaurus?')
        self.type = response
        if response == 'T-Rex':

        elif response == 'Velociraptor':

        elif response == 'Stegosaurus':



    def t_rex_type(self):
        self.health = '80'
        self.energy = '50'
        self.attack_power = '95'

    def velociraptor_type(self):
        self.health = '50'
        self.energy = '120'
        self.attack_power = '60'

    def stegosaurus_type(self):
        self.health = '120'
        self.energy = '60'
        self.attack_power = '75'