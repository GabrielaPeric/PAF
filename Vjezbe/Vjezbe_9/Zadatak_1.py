import numpy as np 
import matplotlib.pyplot as plt
import bungee

a1 = bungee.Bungiee_Jumping()
a1.set_initial_conditions(80,0,100,1,1.225,30,100)  #mass, Cd, k, A, rho, l, h
a1.evolve()

a2 = bungee.Bungiee_Jumping()
a2.set_initial_conditions(80,0.8,100,1,1.225,30,100)
a2.evolve()

plt.subplot(2,2,1)
plt.plot(a1.t,a1.y)

plt.subplot(2,2,2)
plt.plot(a1.t,a1.Potencijalna_energija)
plt.plot(a1.t,a1.Kineticka_energija)
plt.plot(a1.t,a1.Elasticna_energija)
plt.plot(a1.t,a1.Ukupna_energija)

plt.subplot(2,2,3)
plt.plot(a2.t,a2.y)

plt.subplot(2,2,4)
plt.plot(a2.t,a2.Potencijalna_energija)
plt.plot(a2.t,a2.Kineticka_energija)
plt.plot(a2.t,a2.Elasticna_energija)
plt.plot(a2.t,a2.Ukupna_energija)

plt.show()