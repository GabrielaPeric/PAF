import math 
import matplotlib.pyplot as plt
import particle as prt

p1 = prt.Particle()

lista_dt = []
lista_pogreska = []
N = 100
dt = 0.001

for i in range(N):
    p1.set_initial_conditions(0,0,10,60,dt)
    greska = abs(p1.range() - p1.analiticki_domet())/p1.analiticki_domet()*100
    lista_dt.append(p1.dt)
    lista_pogreska.append(greska)
    p1.reset()
    dt += 0.001



plt.plot(lista_dt,lista_pogreska)
plt.show()