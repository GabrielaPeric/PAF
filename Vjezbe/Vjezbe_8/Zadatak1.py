import math
import matplotlib.pyplot as plt
import numpy as np

class Projectile():
    def __init__(self):
        self.x = []
        self.y = []
        self.v_x = []
        self.v_y = []
        self.t = []
        self.a_x = []
        self.a_y = []
        self.rho = []
        self.Cd = []
        self.m = []
        self.A = []

    def set_initial_conditions(self, x0, y0, v0, m, theta, A, rho, Cd, dt):
        self.a_x.append(0)
        self.a_y.append(9.81)
        self.v_x.append(v0*math.cos(math.radians(theta)))
        self.v_y.append(v0*math.sin(math.radians(theta)))
        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.rho.append(rho)
        self.Cd.append(Cd)
        self.m.append(m)
        self.A.append(A)
        self.theta = theta
        self.dt = 0.1

    def reset(self):
        self.x = []
        self.y = []
        self.v_x = []
        self.v_y = []
        self.t = []
        self.a_x = []
        self.a_y = []
        self.rho = []
        self.Cd = []
        self.m = []
        self.A = []

    def akcelerazion_x(self):
        return -np.sign((self.rho[-1]*self.Cd[-1]*self.A[-1])/2*self.m[-1])**self.v_x[-1]

    def akcelerazion_y(self):
        return -self.a_y[-1]-np.sign((self.rho[-1]*self.Cd[-1]*self.A[-1])/2*self.m[-1])**self.v_y[-1]

    

    
