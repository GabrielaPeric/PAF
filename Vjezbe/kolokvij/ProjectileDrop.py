import math
import matplotlib.pyplot as plt 

class ProjectileDrop():
    def __init__(self):
        self.x = []
        self.h = []
        self.v_x = []
        self.v_y = []
        self.t = []
        self.a_x = []
        


    print("Objek je stvoren!")

    def set_initial_conditions(self,h,v_x):
        self.x = [0]
        self.h = [h]
        self.v_x = [v_x]
        self.v_y = [0]
        self.t = [0]
        self.a_x = [0]
        self.a_y = [9.81]
        self.dt = 0.01

        print("Pocetna visina je: {}, a pocetna brzina je: {}".format(self.h[0], self.v_x[0]))

    def promjena_visine(self,h_novi):
        self.h = [h_novi]

        print("Ovo je nova visina: {}".format(self.h[0]))

    def promjena_brzine(self,v_x_novi):
        self.v_x = [v_x_novi]

        print("Ovo je nova brzina: {}".format(self.v_x[0]))

    def __move(self):
        self.t.append(self.t[-1]+self.dt)
        self.a_x.append(self.a_x[-1])
        self.a_y.append(self.a_y[-1])
        self.v_x.append(self.v_x[-1])
        self.v_y.append(self.v_y[-1]-self.a_y[-1]*self.dt)
        self.x.append(self.x[-1]+self.v_x[-1]*self.dt)
        self.h.append(self.h[-1]+self.v_y[-1]*self.dt)

    def kretanje(self):
        while self.h[-1] >= 0:
            self.__move()
        return(self.t, self.v_y, self.x, self.h)

    def grafovi(self):
        plt.subplot(1,2,1)
        plt.plot(self.x,self.h)
        plt.title("x-y graf")

        plt.subplot(1,2,2)
        plt.plot(self.t,self.v_y)
        plt.title("v_y-t graf")
        
        plt.show()


    def vrijeme_trajanja(self):
        while self.h[-1] >= 0:
            self.__move()
        print(self.t[-1])

#p = ProjectileDrop()
#p.__init__()
#p.set_initial_conditions(10,5)
#p.promjena_visine(2000)
#p.promjena_brzine(200)
#p.kretanje()
#p.grafovi()