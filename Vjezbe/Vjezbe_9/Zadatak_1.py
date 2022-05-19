import math
import numpy as np
import matplotlib.pyplot as plt

class Bungee():
    def __init__(self):
        self.y = []
        self.k = []
        self.v = []
        self.A = []
        self.mass = []
        self.l = []
        self.Cd = []
        self.rho = []
        self.t = []
        self.potencijalna_energija = []
        self.kineticka_energija = []
        self.elasticna_energija = []

    
    def set_intial_conditions(self, mass, k, y0, l, v0, A, dt = 0.001, Cd = 0.47, rho = 1.225):
        self.y = [y0]
        self.k = [k]
        self.v = [v0]
        self.A = [A]
        self.mass = [mass]
        self.l = [l]
        self.Cd = [Cd]
        self.rho = [rho]
        self.t = [0]

    def reset(self):
        self.y = []
        self.k = []
        self.v = []
        self.A = []
        self.mass = []
        self.l = []
        self.Cd = []
        self.rho = []

    def __potencijalna_energija(self):
        return (self.mass[-1] * (-9,81)* self.h[-1])

    def __kineticka_energija(self):
        return((self.mass*self.v[-1]**2)/2)

    def __elasticna_energija(self):
        if self.y[-1] <= self.l[0]:
            return(-self.k[0]*self.y[-1])
        else:
            return(0)

    
    