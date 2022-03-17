import numpy as np 
import math 
import matplotlib.pyplot as plt 

v0 = 10  
theta = 60 
v0_x = v0*math.cos((theta/360)*2*np.pi)
v0_y = v0*math.sin((theta/360)*2*np.pi)
t = np.arange(0.0, 10.5, 0.5) #za prvih deset sekundi 
t_list = t.tolist()
x = [0]
y = [0]
v_x = [v0_x] #brzina je konstantna u x smjeru
v_y = [v0_y]
a_x = [0] #brzina konstanta pa nema akceleracije
a_y = [9.81] #ovo je g akceleracija, slobodni pad, akceleracija je konstanta
interval = 0.5

for i in range(len(t_list) -1 ):
    a_x.append(0)
    a_y.append(9.81)
    v_x.append(v0_x)
    v_y.append(v_y[i]-a_y[i]*interval)
    x.append(x[i]+v_x[i+1]*interval)
