import math
from tkinter.tix import Tree
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
        self.udaljenost = 0
        self.udaljenost_lista = []
        self.kut_lista = []

    def set_initial_conditions(self, x0, y0, v0, m, theta, rho, Cd, dt, r_or_a, izbor):
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
        self.r_or_a = r_or_a
        self.izbor = izbor
        if self.izbor == "kugla":
            self.A.append((r_or_a**2)*math.pi)
        elif self.izbor == "kocka":
            self.A.append(r_or_a**2)
        else:
            print("Izbor mora biti ili kugla ili kocka xD")
        self.theta = theta
        self.dt = dt 
        self.v0 = v0

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

    def akceleracija_x(self,x,v,t):
        return -np.sign(v)*((self.rho[-1]*self.Cd[-1]*self.A[-1])/(2*self.m[-1]))*v**2

    def akceleracija_y(self,x,v,t):
         return -9.81-np.sign(v)*((self.rho[-1]*self.Cd[-1]*self.A[-1])/(2*self.m[-1]))*v**2

    def __Euler(self):
        self.t.append(self.t[-1]+self.dt)
        self.a_x.append(-np.sign(self.v_x[-1])*(self.rho[-1]*self.Cd[-1]*self.A[-1])/(2*self.m[-1])*(self.v_x[-1])**2)
        self.a_y.append(-9.81-np.sign(self.v_y[-1])*(self.rho[-1]*self.Cd[-1]*self.A[-1])/(2*self.m[-1])*(self.v_y[-1])**2)
        #self.a_x.append(self.akceleracija_x(self.x[-1],self.v_x[-1],self.t[-1]))
        #self.a_y.append(self.akceleracija_y(self.x[-1],self.v_x[-1],self.t[-1]))
        self.v_x.append(self.v_x[-1]+self.a_x[-1]*self.dt)
        self.v_y.append(self.v_y[-1]+self.a_y[-1]*self.dt)
        self.x.append(self.x[-1]+self.v_x[-1]*self.dt)
        self.y.append(self.y[-1]+self.v_y[-1]*self.dt)

    def __runge_kutta(self):
        k1_v_x = self.akceleracija_x(self.x[-1],self.v_x[-1],self.t[-1])*self.dt
        k1_v_y = self.akceleracija_y(self.y[-1],self.v_y[-1],self.t[-1])*self.dt
        k1_x = self.v_x[-1]*self.dt
        k1_y = self.v_y[-1]*self.dt
        
        k2_v_x = self.akceleracija_x(self.x[-1]+k1_x/2,self.v_x[-1]+k1_v_x/2,self.t[-1]+self.dt/2)*self.dt
        k2_v_y = self.akceleracija_y(self.y[-1]+k1_y/2,self.v_y[-1]+k1_v_y/2,self.t[-1]+self.dt/2)*self.dt
        k2_x = (self.v_x[-1] + k1_v_x/2)*self.dt
        k2_y = (self.v_y[-1] + k1_v_y/2)*self.dt

        k3_v_x = self.akceleracija_x(self.x[-1]+k2_x/2,self.v_x[-1]+k2_v_x/2,self.t[-1]+self.dt/2)*self.dt
        k3_v_y = self.akceleracija_y(self.y[-1]+k2_y/2,self.v_y[-1]+k2_v_y/2,self.t[-1]+self.dt/2)*self.dt
        k3_x = (self.v_x[-1]+k2_v_x/2)*self.dt
        k3_y = (self.v_y[-1]+k2_v_y/2)*self.dt

        k4_v_x = self.akceleracija_x(self.x[-1]+k3_x, self.v_x[-1]+k3_v_x,self.t[-1]+self.dt)*self.dt
        k4_v_y = self.akceleracija_y(self.y[-1]+k3_y, self.v_y[-1]+k3_v_y, self.t[-1]+self.dt)*self.dt
        k4_x = (self.v_x[-1]+k3_v_x)*self.dt
        k4_y = (self.v_y[-1]+k3_v_y)*self.dt
        
        self.v_x.append(self.v_x[-1]+ (1/6)*(k1_v_x+2*k2_v_x+2*k3_v_x+k4_v_x))
        self.v_y.append(self.v_y[-1]+ (1/6)*(k1_v_y+2*k2_v_y+2*k3_v_y+k4_v_y))
        
        self.x.append(self.x[-1] + (1/6)*(k1_x+2*k2_x+2*k3_x+k4_x))
        self.y.append(self.y[-1] + (1/6)*(k1_y+2*k2_y+2*k3_y+k4_y))
        
        self.t.append(self.t[-1]+self.dt)


    def evolve_Euler(self):
        while self.y[-1] >= 0:
            self.__Euler()
        return (self.x , self.y)
        
    def evolve_runge_kutta(self):
        while self.y[-1] >= 0:
            self.__runge_kutta()
        return (self.x , self.y)

    
    def domet_Euler(self):
        while self.y[-1] >= 0:
            self.__Euler()
        return self.x[-1]


    def domet_runge_kutta(self):
        while self.y[-1] >= 0:
            self.__runge_kutta()
        return self.x[-1]


    def hit_the_target(self,x_meta,y_meta,radijus_mete):
        pogodjena = False
        while self.y[-1] >= 0:
            self.__runge_kutta()
            self.udaljenost_lista.append(math.sqrt((x_meta - self.x[-1])**2 + (y_meta - self.y[-1])**2))
        self.udaljenost = min(self.udaljenost_lista)
        if self.udaljenost <= radijus_mete:
            pogodjena = True
            #print("Meta je pogodjena")
        else:
            #print("meta nije pogodjena")
            pass
        
        #if pogodjena == True:
            #print("Meta je pogodjena")
        #else:
            #print("Meta nije pogodjena")


    def angle_to_hit_the_target(self,x_meta,y_meta,radijus_mete):
        pogodjena = False
        
        for i in range(91):
            self.kut = i*math.pi/180
            self.v_x.append(self.v0*math.cos(math.radians(i)))
            self.v_y.append(self.v0*math.sin(math.radians(i)))

            while self.y[-1] >= 0:
                self.__runge_kutta()
                self.udaljenost_lista.append(math.sqrt((x_meta - self.x[-1])**2 + (y_meta - self.y[-1])**2))
            self.udaljenost = min(self.udaljenost_lista)
            if self.udaljenost <= radijus_mete:
                pogodjena = True
                #print("Meta je pogodjena i kut je {}".fomrat(i))
            else:
                #print("meta nije pogodjena")
                pass       
        if pogodjena == True:
            print("Meta je pogodjena")
        else:
            print("Meta nije pogodjena")
            
        



a = Projectile()
a.set_initial_conditions(0,0,10,10,50,1.3,0.5,0.01,2,"kugla") # x0, y0, v0, m, theta, rho, Cd, dt, r_or_a, izbor
#a.evolve_runge_kutta()
a.angle_to_hit_the_target(4,3.5,2)