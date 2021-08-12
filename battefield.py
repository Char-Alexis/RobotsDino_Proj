from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.herd.create_herd
        self.fleet= Fleet()
        self.fleet.create_fleet() 
        # create an empty fleet, fills list with 3 robots

    def run_game(self):
        self.battle()

    def display_welcome(self):
        print("Welcome to Robots vs. Dinosaurs!")

    def battle(self):
        total_herd_health = 0
        for dinosaur in self.herd.dinosaurs:
            total_herd_health = total_herd_health + dinosaur.health.status()

            while total_herd_health > 0:
                self.robo_turn(self.fleet.robots[0])

                for dinosaur in self.herd.dinosaurs:
                    total_herd_health = total_herd_health + dinosaur.health.status()



    def dino_turn(self, dinosaur):
        for robot in self.fleet.robots:
            if robot.health.status() !=0:
                dinosaur.attack(robot)
                break
                

    def robo_turn(self, robot):
        for dinosaur in self.herd.dinosaurs:
            robot.attack(dinosaur)

    def show_dino_opponent_options(self):
        for robot in self.fleet.robots:
            if robot.health.status() != 0:
                print(robot.name + "is not dead, can be attacked.")

    def show_robo_opponent_options(self):
        for dinosaur in self.herd.dinosaurs:
            if dinosaur.health_status() != 0:
                print(dinosaur.name + "is not dead, can be attacked.")


    def display_winners(self):
        # total_fleet_health = 5
        # total_herd_health = 0

        for robot in self.fleet.robots:
            total_fleet_health = total_fleet_health + robot.health_status()

        for dinosaur in self.herd.dinosaurs:
            total_herd_health = total_herd_health + dinosaur.health_status()

            if total_herd_health > total_fleet_health:
                print("The dinosaurs are victorious!")

            elif total_fleet_health > total_herd_health:
                print("The robots are victorious!")

            else:
                print("It's a draw!")
