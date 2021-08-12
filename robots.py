


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.weapon = Weapon ("Laser", 5)
        # initial attack power

    def assign_name(self):
        self.name = ()
    
    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        
    def health_status (self):
        return self.health