import math
import numpy as np

def maksimalna_visina (v0,theta,x0,y0):
    y = [y0]
    v0_y = v0*math.sin((theta/360)*2*math.pi)
    v_y = [v0_y]
    t = np.arange(0.0, 10.1, 0.1) 
    t_list = t.tolist()
    a_y = [9.81]
    interval = 0.1
    
    for i in range(len(t_list) -1 ):
        a_y.append(9.81)
        v_y.append(v_y[i]-a_y[i]*interval)
        y.append(y[i]+v_y[i+1]*interval)
    max_visina = max(y)
    print("Maksimalana visina je {}".format(max_visina))

def domet(v0,theta,x0,y0):
    v0_x = v0*math.cos((theta/360)*2*math.pi)
    v0_y = v0*math.sin((theta/360)*2*math.pi)
    v_y = v0_y
    interval = 0.1
    x = x0
    y = y0
    a_y = 9.81
    a_x = y0
    while True:
        x = x + v0_x*interval
        v_y = v_y - a_y*interval
        y = y + v_y*interval
        if y<= 0:
            break
    print("Domet je {}".format(x))

def max_brzina(v0, theta,x0,y0):
    v0_x = v0*math.cos((theta/360)*2*math.pi)
    v0_y = v0*math.sin((theta/360)*2*math.pi)    
    x = x0
    y = y0
    v_x = v0_x 
    v_y = v0_y
    a_x = 0 
    a_y = 9.81
    interval = 0.1

    while True:
        x = x+v_x*interval
        v_y = v_y - a_y*interval
        if y <= 0:
            break
    v = math.sqrt(v_y**2+v_x**2)
    print("Maksimalna brzina je {}".format(v))
