from robots import Robot


class Fleet:
    def __init__(self):
        self.robots = []
# stores robot objects

    def create_fleet(self):

        for i in range(3)
            name = "Robot" + str(i + 1)
            self.robots.append(Robot(name))