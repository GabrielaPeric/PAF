import math 
import matplotlib.pyplot as plt
import particle as prt

p1 = prt.Particle(0,0,10,60)
p1.set_initial_conditions(0,0,10,60)
dt = 0.0
lista_dt = []
lista_pogreska = []
N = 10

for i in range(N):
    dt += 0.1
    gr = p1.relativna_pogreska()
    lista_dt.append(dt)
    lista_pogreska.append(gr)
    p1.reset()

print(lista_dt)
print(lista_pogreska)

plt.plot(lista_dt,lista_pogreska)
plt.show()