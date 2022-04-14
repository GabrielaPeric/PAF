import matplotlib.pyplot as plt

class Gibanje:
    def __init__(self):
        self.t = []
        self.x = []
        self.v = []
        self.a = []
        self.dt = 0
        self.m = []
        self.func = 0
        
        
    def set_initial_conditions(self,func,x,v,m,dt=0.1):
        self.t = [0]
        self.x = [x]
        self.v = [v]
        self.m = [m]
        self.dt = dt
        self.func = func
        self.F = (self.func(self.v[-1], self.x[-1],self.t[-1]))
        self.a.append(self.F/self.m[-1])
        
    def reset(self):
        self.t = []
        self.x = []
        self.v = []
        self.a = []
        self.dt = 0
        
    def __move(self,t_ukupno = 5):
        while self.t[-1] <= t_ukupno:
            self.t.append(self.t[-1]+self.dt)
            self.v.append(self.v[-1]+self.a[-1]*self.dt)
            self.x.append(self.x[-1]+self.v[-1]*self.dt)
            self.F = self.func(self.v[-1],self.x[-1],self.t[-1])
            self.a.append(self.F/self.m[-1])
            
            
    def print(self):
        self.__move()
        print(self.t, self.x, self.v)