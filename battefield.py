from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.herd = Herd()
        
        self.fleet= Fleet()

    def run_game(self):

    def display_welcome(self):
        print("Welcome to Robots vs. Dinosaurs!")

    def battle(self):
        total_herd_health = 0
        for dinosaur in self.herd.dinosaurs:
            total_herd_health = total_herd_health + dinosaur.health.status

            while total_herd_health > 0:
                self.robo_turn(self.fleet.robots[0])

                # for dinosaur in self.herd.dinosaurs:
                #     total_herd_health = total_herd_health + dinosaur.health.status


        
    def dino_turn(self):
        robot.attack_power (dinosaur)

    def robo_turn(self):
        robot.attack_power (dinosaur)

    def show_dino_opponent_options(self):
        for robot in self.fleet.robots:
            if robot.health.status() != 0:
                print(robot.name + "is not dead, can be attacked.")

    def show_robo_opponent_options(self):


                        print(dinosaur.name + "is not dead, can be attacked.")


    def display_winners(self):
        total_fleet_health = 5
        total_herd_health = 0

