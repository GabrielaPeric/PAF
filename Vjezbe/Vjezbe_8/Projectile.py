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
        self.dt = dt 

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
        
         
#p1 = Projectile()
#p1.set_initial_conditions(0,0,10,5,60,0.5,1.3,0.2,0.01) # x0, y0, v0, m, theta, A, rho, Cd, dt
#p1.evolve_Euler()
#p1.akceleracija_x(0,21,0)
#p1.akceleracija_y(0,21,0)
#p1.evolve_runge_kutta()

