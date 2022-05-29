import numpy as np 
import matplotlib.pyplot as plt 
import math 

class Particle():
    def __init__(self):
        #self.x_sun = []
        #self.x_earth = []
        #self.y_sun = []
        #self.y_earth = []
        #self.v_x_sun = []
        #self.v_x_earth = []
        #self.v_y_sun = []
        #self.v_y_earth = []
        #self.a_x_sun = []
        #self.a_x_earth = []
        #self.a_y_sun = []
        #self.a_y_earth = []
        self.t = [0]
        self.dt = 60*60*24
        self.total_time = 365.242 * self.dt
        self.r_sun = np.array [[0,0]]
        self.r_earth = np.array [[0,0]]
        self.v_sun = [[0,0]]
        self.v_earth = [[0,0]]
        self.a_sun = [[0,0]]
        self.a_earth = [[0,0]]

    def set_initial_conditions(self,x_sun = 0, y_sun = 0, x_earth = 1.486*(10**11), y_earth = 0, v_x_sun = 0, v_y_sun = 0, v_x_earth = 0, v_y_earth = 29783, a_x_sun = 0, a_y_sun = 0, a_x_earth = 0, a_y_earth = 0):
        self.mass_sun = 1.989*(10**30) 
        self.mass_earth = 5.9742*(10**24)
        self.gravitacijska_konstanta = 6.67408 *(10**(-11))
        #self.x_sun = [x_sun]
        #self.y_sun = [y_sun]
        #self.x_earth = [x_earth]
        #self.y_earth = [y_earth]
        #self.v_x_sun = [v_x_sun]
        #self.v_y_sun = [v_y_sun]
        #self.v_x_earth = [v_x_earth]
        #self.v_y_earth = [v_y_earth]
        self.r_sun = np.array [[x_sun,y_sun]]
        self.r_earth = np.array [[x_earth,y_earth]]
        self.v_sun = [[v_x_sun, v_y_sun]]
        self.v_earth = [[v_x_earth, v_y_earth]]
        self.a_sun = [[a_x_sun, a_y_sun]]
        self.a_earth = [[a_x_earth, a_y_earth]]

    def __move(self):
        self.a_sun.append(-self.gravitacijska_konstanta*(self.mass_earth/(np.abs(np.subtract(self.r_sun - self.r_earth)))**3))
        self.a_earth.append(-self.gravitacijska_konstanta*(self.mass_sun/(np.abs(np.subtract(self.r_earth - self.r_sun)))**3))
        self.v_sun.append(self.v_sun[-1]+self.a_sun[-1]*self.dt)
        self.v_earth.append(self.v_earth[-1]+self.a_earth[-1]*self.dt)
        self.r_sun.append(self.r_sun[-1]+self.v_sun[-1]*self.dt)
        self.r_earth.append(self.r_earth[-1]+self.v_earth[-1]*self.dt) 
        self.t.append(self.t[-1]+self.dt)