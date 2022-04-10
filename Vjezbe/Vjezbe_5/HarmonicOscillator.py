import math
import matplotlib.pyplot as plt

class HarmonicOscillator():
    def __init__(self):
        self.x = []
        self.v = []
        self.t = []
        self.a = []
        self.m = []
        self.k = []
        self.dt = 0
        
    def set_initial_conditions(self,x,v,k,m,dt):
        self.x = [x]
        self.v = [v]
        self.k = [k]
        self.m = [m]
        self.t = [0]
        self.a.append(k*self.x[-1]/m)
        self.dt = dt

    def reset(self):
        self.x = []
        self.v = []
        self.t = []
        self.a = []
        self.m = []
        self.k = []
        self.dt = 0.1
    
    def __move(self):
        self.t.append(self.t[-1]+self.dt)
        self.a.append(-self.k[-1]*self.x[-1]/self.m[-1])
        self.v.append(self.v[-1]+self.a[-1]*self.dt)
        self.x.append(self.x[-1]+self.v[-1]*self.dt)
        
    def oscillate(self,t):
        while self.t[-1]<=t:
            self.__move()

    def plot_trajectory(self):
        plt.subplot(1,3,1)
        plt.plot(self.t,self.x)
        plt.title("x-t graf")

        plt.subplot(1,3,2)
        plt.plot(self.t,self.v)
        plt.title("v-t graf")

        plt.subplot(1,3,3)
        plt.plot(self.t,self.a)
        plt.title("a-t graf")

        plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

        plt.show()
    
    def period(self):
        T = 0
        while True:
            self.__move()
            if self.x[-1] < 0:
                T = 0
                break
        while True:
            self.__move()
            T += self.dt
            if self.x[-1]> 0:
                break
        print (2*T)

    
    def period_analitic(self):
        d = 2*math.pi*math.sqrt(self.m[0]/self.k[0])
        print(d) 
        
        
#p = HarmonicOscillator()
#p.set_initial_conditions(0,10,4,5,0.1)
#p.oscillate(10)
#p.plot_trajectory()
#p.period()  

