import numpy as np 

class EmField:
    def __init__(self):
        self.x_lista = []
        self.y_lista = []
        self.z_lista = []
        self.t_lista = [0]
        self.dt = 0.01
        
    def set_initial_conditions(self,mass,q,r,v,E,func):
        self.mass = mass
        self.q = q 
        self.r = r 
        self.v = v
        self.E = E
        self.func = func
        self.B = self.func(self.t_lista[-1])
        self.x_lista.append(self.r[0])
        self.y_lista.append(self.r[1])
        self.z_lista.append(self.r[2])
        self.a = self.__akceleracija(self.v,self.B)
    
    def reset(self):
        self.x_lista = []
        self.y_lista = []
        self.z_lista = []
        self.t_lista = []
        
    def __akceleracija(self,v,B):
        return (self.q/self.mass) * (np.add(self.E,np.cross(v,B)))
    
    
    def __runge_kutta(self):
        k1_v = self.__akceleracija(self.v,self.B)*self.dt
        k1_r = self.v*self.dt
        
        k2_v = self.__akceleracija(np.add(self.v,k1_v/2),self.B)*self.dt
        k2_r = (np.add(self.v,k1_v/2))*self.dt
        
        k3_v = self.__akceleracija(np.add(self.v,k2_v/2),self.B)*self.dt
        k3_r = (np.add(self.v,k2_v/2))*self.dt
        
        k4_v = self.__akceleracija(np.add(self.v,k3_v/2),self.B)*self.dt
        k4_r = (np.add(self.v,k3_v/2))*self.dt
        
        self.v = np.add(self.v,(1/6)*np.add(np.add(k1_v,2*k2_v),np.add(2*k3_v,k4_v))) #np.add prima samo dva argumenta
        self.r = np.add(self.r,(1/6)*np.add(np.add(k1_r,2*k2_r),np.add(2*k3_r,k4_r)))
        self.a = self.__akceleracija(self.v,self.B)
        self.t_lista.append(self.t_lista[-1] + self.dt)
        
    def evolve_runge_kutta(self,total_time):
        self.total_time = total_time
        while self.t_lista[-1] <= self.total_time:
            self.B = self.func(self.t_lista[-1])
            self.__runge_kutta()
            self.x_lista.append(self.r[0])
            self.y_lista.append(self.r[1])
            self.z_lista.append(self.r[2])
        
        return self.x_lista, self.y_lista, self.z_lista

