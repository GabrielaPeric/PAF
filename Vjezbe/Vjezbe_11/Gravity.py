import numpy as np 
import matplotlib.pyplot as plt 
import math 

class Gravity():
    def __init__(self):
        self.t = [0]
        self.dt = 60*60*24
        self.total_time = 365.242 * self.dt
        self.r_sun = np.array ((0,0))
        self.r_earth = np.array ((0,0))
        self.v_sun = np.array ((0,0))
        self.v_earth = np.array ((0,0))
        self.a_sun = np.array ((0,0))
        self.a_earth = np.array ((0,0))
        self.x_sun_lista = []
        self.y_sun_lista = []
        self.x_earth_lista = []
        self.y_earth_lista = []

    def set_initial_conditions(self,x_sun = 0, y_sun = 0, x_earth = 1.496*(10**(11)), y_earth = 0, v_x_sun = 0, v_y_sun = 0, v_x_earth = 0, v_y_earth = 29783, a_x_sun = 0, a_y_sun = 0, a_x_earth = 0, a_y_earth = 0):
        self.mass_sun = 1.989*(10**30) 
        self.mass_earth = 5.9742*(10**24)
        self.gravitacijska_konstanta = 6.67408 *(10**(-11))
        #self.astronomska_jedninica = 1.496*10**(11) #self.r_sun - self.r_earth
        self.r_sun =  np.array((x_sun,y_sun))
        self.r_earth = np.array((x_earth,y_earth))
        self.v_sun = np.array((v_x_sun,v_y_sun))
        self.v_earth = np.array((v_x_earth,v_y_earth))
        self.a_sun = np.array((a_x_sun,a_y_sun))
        self.a_earth = np.array((a_x_earth,a_y_earth))
        self.x_sun_lista.append(self.r_sun[0])
        self.y_sun_lista.append(self.r_sun[1])
        self.x_earth_lista.append(self.r_earth[0])
        self.y_earth_lista.append(self.r_earth[1])


    def __move(self):
        self.a_sun = (-self.gravitacijska_konstanta*(self.mass_earth/(np.abs(np.subtract(self.r_sun, self.r_earth)))**3))*(np.sign(np.subtract(self.r_sun, self.r_earth)))
        self.a_earth = (-self.gravitacijska_konstanta*(self.mass_sun/(np.abs(np.subtract(self.r_earth, self.r_sun)))**3))*(np.sign(np.subtract(self.r_earth, self.r_sun)))
        self.v_sun = (np.add(self.v_sun,self.a_sun*self.dt))
        self.v_earth = (np.add(self.v_earth,self.a_earth*self.dt))
        self.r_sun = (np.add(self.r_sun,self.v_sun*self.dt))
        self.r_earth = (np.add(self.r_earth,self.v_earth*self.dt))
        self.t.append(self.t[-1]+self.dt)

    def Evolve(self):
        while self.t[-1] <= self.total_time:
            self.__move()
            self.x_sun_lista.append(self.r_sun[0])
            self.y_sun_lista.append(self.r_sun[1])
            self.x_earth_lista.append(self.r_earth[0])
            self.y_earth_lista.append(self.r_earth[1])
        
        return self.x_sun_lista, self.y_sun_lista, self.x_earth_lista, self.y_earth_lista

p1 = Gravity()
p1.set_initial_conditions()
p1.Evolve()

plt.plot(p1.x_sun_lista, p1.y_sun_lista, p1.x_earth_lista, p1.y_earth_lista)
plt.show()
    