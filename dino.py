class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 10

    def attack(self, robot):
        robot.health = robot.health - self.attack_power

    def health_status(self):
        return self.health