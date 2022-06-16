import numpy as np
import math 
import matplotlib.pyplot as plt

class Bungiee_Jumping():
    def __init__(self):
        self.t = []
        self.y = []
        self.v = []
        self.a = []

        self.x_lista = []
        self.rho = []
        self.Cd = []
        self.mass = []
        self.area = []
        self.g = []
        self.l = []
        self.k = []
        self.h = []

        self.Kineticka_energija = []
        self.Potencijalna_energija = []
        self.Elasticna_energija = []
        self.Ukupna_energija = []

    def set_initial_conditions(self, mass, Cd, k, A, rho, l, h):
        self.t.append(0)
        self.y.append(h)
        self.v.append(0)
        self.a.append(-9.81)
        
        self.rho.append(rho)
        self.Cd.append(Cd)
        self.mass.append(mass)
        self.area.append(A)
        self.g.append(-9.81)
        self.l.append(l)
        self.k.append(k)
        self.h.append(h)

        self.dt = 0.001


        self.Kineticka_energija.append(0.5*self.mass[0]*(self.v[0]**2))
        self.Potencijalna_energija.append(np.abs(self.mass[0]*self.g[0]*self.h[0]))
        self.Elasticna_energija.append(0.5*self.k[0]*0)
        self.Ukupna_energija.append(self.Kineticka_energija[-1]+self.Potencijalna_energija[-1]+self.Elasticna_energija[-1])

    def reset(self):
        self.__init__()
        
    def __acceleration(self,y,v,t):
        if y < self.h[0] - self.l[0]:
            dx = (y+self.l[0])-self.h[-1]
        else:
            dx = 0
        
        return -9.81 -self.k[-1]*dx/self.mass[-1] - 1*np.sign(v)*((self.rho[-1]*self.Cd[-1]*self.area[-1])/(2*self.mass[-1]))*v*v

    def __energy(self,y,v):
        if y < self.h[0] - self.l[0]:
            dx = (y+self.l[0])-self.h[-1]
        else:
            dx = 0


        self.Elasticna_energija.append(0.5*self.k[-1]*dx**2)
        self.Potencijalna_energija.append(np.abs(self.mass[-1]*9.81*y))
        self.Kineticka_energija.append((1/2)*self.mass[-1]*v*v)
        self.Ukupna_energija.append(self.Elasticna_energija[-1]+self.Kineticka_energija[-1]+self.Potencijalna_energija[-1])

    def __move(self):
        k1_v = (self.__acceleration(self.y[-1], self.v[-1], self.t[-1]))*self.dt
        k1_y = self.v[-1]*self.dt
        k2_v = self.__acceleration(self.y[-1]+k1_y/2,self.v[-1]+k1_v/2,self.t[-1]+self.dt/2)*self.dt
        k2_y = (self.v[-1]+k1_v/2)*self.dt
        k3_v = self.__acceleration(self.y[-1]+k2_y/2,self.v[-1]+k2_v/2,self.t[-1]+self.dt/2)*self.dt 
        k3_y = (self.v[-1]+k2_v/2)*self.dt
        k4_v = self.__acceleration(self.y[-1]+k3_y,self.v[-1]+k3_v,self.t[-1]+self.dt)*self.dt
        k4_y = (self.v[-1]+k3_v)*self.dt

        self.v.append(self.v[-1]+(k1_v+2*k2_v+2*k3_v+k4_v)/6)
        self.y.append(self.y[-1]+(k1_y+2*k2_y+2*k3_y+k4_y)/6)
        self.t.append(self.t[-1]+self.dt)
        
        self.__energy(self.y[-1],self.v[-1])

    def evolve(self, total_time = 30):
        while self.t[-1] <= total_time and self.y[-1] > 0:
            self.__move()
        return self.t, self.y, self.Elasticna_energija, self.Kineticka_energija, self.Potencijalna_energija

    def plot_y(self):
        self.evolve()
        plt.plot(self.t,self.y)
        plt.show()

    def plot_energija(self):
        self.evolve()
        plt.plot(self.t, self.Potencijalna_energija, "r")
        plt.plot(self.t, self.Kineticka_energija, "b")
        plt.plot(self.t, self.Elasticna_energija, "y")
        plt.plot(self.t,self.Ukupna_energija, "k")
        plt.show()


#a1 = Bungiee_Jumping()
#a1.set_initial_conditions(80,0,100,1,1.225,30,100)  #mass, Cd, k, A, rho, l, h
#a1.plot_y()
#a1.plot_energija()