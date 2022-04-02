import math 
import matplotlib.pyplot as plt
class Particle():
    def __init__(self,x0,y0,v0,theta):
        self.x = []
        self.y = []
        self.v_x = []
        self.v_y = []
        self.t = []
        self.a_x = []
        self.a_y = []
        self.theta = theta
        self.dt = 0.1
    
    def set_initial_conditions(self, x0,y0,v0,theta):
        self.a_x.append(0)
        self.a_y.append(9.81)
        self.v_x.append(v0*math.cos(math.radians(theta)))
        self.v_y.append(v0*math.sin(math.radians(theta)))
        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
    
    def reset(self):
        self.x = []
        self.y = []
        self.v_x = []
        self.v_y = []
        self.t = []
        self.a_x = []
        self.a_y = []
        self.dt = 0.1
    
    def __move(self):
        self.t.append(self.t[-1]+self.dt)
        self.a_x.append(self.a_x[-1])
        self.a_y.append(self.a_y[-1])
        self.v_x.append(self.v_x[-1])
        self.v_y.append(self.v_y[-1]-self.a_y[-1]*self.dt)
        self.x.append(self.x[-1]+self.v_x[-1]*self.dt)
        self.y.append(self.y[-1]+self.v_y[-1]*self.dt)
        
    
    def range(self):
        while self.y[-1] >= 0:
            self.__move()
        return self.x[-1]

    def plot_trajectory(self):
        plt.plot(self.x,self.y)
        plt.show()
    
    def analiticki(self):
        self.v_y_broj = self.v_y[0]
        self.v_x_broj = self.v_x[0]
        v0 = math.sqrt((self.v_y_broj)**2+(self.v_x_broj)**2)
        theta = math.radians(self.theta)
        domet = v0**2*math.sin(2*theta)/9.81
        return domet

    def relativna_pogreska(self):
        pogreska = (abs(self.analiticki() - self.range())/self.analiticki())*100
        return pogreska

    def total_time(self):
        while self.y[-1] >= 0:
            self.__move()
        print(self.t[-1])

    def max_speed(self):
        while self.y[-1] >= 0:
            self.__move()
        x_najbrza = (max(self.v_x))
        y_najbrza = (max(self.v_y))
        v_najbrza = math.sqrt(x_najbrza**2+y_najbrza**2)
        print(v_najbrza)

    def domet_brzina_graf(self):
        plt.plot()

    


p2 = Particle(0,0,10,60)
p2.set_initial_conditions(0,0,10,60)
p2.total_time()
p2.max_speed()
