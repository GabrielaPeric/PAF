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
            
            
    def print(self):
        self.__move()
        print(self.t, self.x, self.v, self.a)