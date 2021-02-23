class DistanceBetween:
    def __init__(self, name,distance):
        self.state = name
        self.distance = distance

    def __str__(self):
        return "para {} leva {} km".format(self.state, self.distance)
