import math
import numpy as np
import matplotlib.pyplot as plt

class Bungee_jumping():
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
        self.ukupna_energija =[]
        self.x_lista = []
        
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
        self.total_time = 5
        self.dt = dt
        
    
    def reset(self):
        self.y = []
        self.k = []
        self.v = []
        self.A = []
        self.mass = []
        self.l = []
        self.Cd = []
        self.rho = []
    
    def akceleracija(self,x,v,t):
        return self.g - ((np.sign(v)*self.Cd[-1]*self.A[-1]*self.rho[-1]*(v)**2)/(2*self.mass)) - (self.k[-1]*self.x[-1]/self.mass[-1])
    
    def __move(self):
        self.x = 0
        
        while self.t[-1] < self.total_time:
            
            if self.y[-1] < self.h - self.l[-1]:
                self.x = self.y[0] - self.l[0] - self.y[-1]
                self.x_lista.append(self.x)
            else:
                self.x_lista.append(0)
                
            
            k1_v = self.akceleracija(self.x[-1],self.v[-1],self.t[-1])*self.dt
            k1_y = self.v[-1]*self.dt
            
            k2_v = self.akceleracija(self.x[-1]+k1_y/2,self.v[-1]+k1_v/2,self.t[-1]+self.dt/2)*self.dt
            k2_y = (self.v[-1] + k1_v/2)*self.dt
            
            k3_v = self.akceleracija(self.x[-1]+k2_y/2,self.v[-1]+k2_v/2,self.t[-1]+self.dt/2)*self.dt
            k3_y = (self.v[-1]+k2_v/2)*self.dt
            
            k4_v = self.akceleracija(self.x[-1]+k3_y, self.v[-1]+k3_v,self.t[-1]+self.dt)*self.dt
            k4_y = (self.v[-1]+k3_v)*self.dt
            
            self.v.append(self.v[-1]+ (1/6)*(k1_v+2*k2_v+2*k3_v+k4_v))
            self.y.append(self.y[-1] + (1/6)*(k1_y+2*k2_y+2*k3_y+k4_y))
            self.t.append(self.t[-1]+self.dt)
            
    def __potencijalna_energija(self):
        self.potencijalna_energija.append(self.mass[-1] * (-9,81)* self.h[-1])

    def __kineticka_energija(self):
        self.kineticka_energija.append((self.mass*self.v[-1]**2)/2)
        
    def __elasticna_energija(self):
        self.elasticna_energija.append(-self.k*self.x[-1])
        
    def __ukupna_energija(self):
        self.__potencijalna_energija()
        self.__kineticka_energija()
        self.__elasticna_energija()
        self.__ukupna_energija = self.potencijalna_energija + self.kineticka_energija + self.elasticna_energija
        
    def plot_y(self):
        while self.t[-1] <= self.total_time:
            self.__move()
        plt.plot(self.t, self.y)
        
    def plot_energija(self):
        while self.t[-1] <= self.total_time:
            self.__move()
            self.__potencijalna_energija()
            self.__kineticka_energija()
            self.__elasticna_energija()
            self.__ukupna_energija()
        plt.plot(self.t,self.potencijalna_energija)
        plt.plot(self.t,self.kineticka_energija)
        plt.plot(self.t,self.elasticna_energija)
        plt.plot(self.t,self.ukupna_energija)
    
    