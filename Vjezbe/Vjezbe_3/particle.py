import math 
class Particle():
    def __init__(self,x0,y0,v0,theta):
        self.x = []
        self.y = []
        self.v_x = []
        self.v_y = []
        self.t = []
        self.a_x = []
        self.a_y = []
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
        self.a_x.append(self.a_x)
        self.a_y.append(self.a_y)
        self.v_x.append(self.v_x)
        self.v_y.append(self.v_y[-1]-self.a_y[-1]*self.dt)
        self.x.append(self.x[-1]+self.v_x[-1]*self.dt)
        self.y.append(self.y[-1]+self.v_y[-1]*self*dt)
        
    
    def range(self):
        while self.y[-1] > 0:
            self.__move()
        return self.x[-1]

    def PrintInfo(self):
        print("v_y je {}".format (self.v_y))
        print("a_x je {}".format(self.a_x))
        print("v_x je {}".format(self.v_x))



p1 = Particle(0,0,15,40)
p1.set_initial_conditions(0,0,15,40)
p1.PrintInfo()
p1.reset()
p1.PrintInfo()
