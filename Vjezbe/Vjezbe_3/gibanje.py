import math 
import matplotlib.pyplot as plt
import particle as prt

p1 = prt.Particle(0,0,10,60)
p1.set_initial_conditions(0,0,10,60)
lista_dt = []
lista_pogreska = []
N = 100
dt = 0.0

for i in range(N):
    dt += 0.01
    lista_dt.append(dt)
    lista_pogreska.append(p1.relativna_pogreska())

print(lista_dt)
print(lista_pogreska)

plt.plot(lista_dt,lista_pogreska)
plt.show()