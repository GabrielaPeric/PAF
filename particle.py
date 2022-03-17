class Particle:
    def __init__(self, mass, x_0):
        self.mass = mass
        self.x_0 = x_0

    def printInfo(self):
        print("Čestiva ima masu {0:.2f} i u pocetnom trenutku nalazi se na polozaju x={1:.2f}".format(self.mass, self.x_0))
