from dino import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):

        for i in range(3):
            name = "Dinosaur" + str(i + 1)
            self.dinosaurs.append(Dinosaur(name, 2))

    # Robot1, Robot2, Robot3 
    # attack power is 2pts