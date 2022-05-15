import math
import numpy as np
import matplotlib.pyplot as plt 
import Projectile


p1 = Projectile.Projectile()
p1.set_initial_conditions(0,0,10,5,60,0.5,1.3,0.2,0.01) 
x1, y1 = p1.evolve_Euler()

p2 = Projectile.Projectile()
p2.set_initial_conditions(0,0,10,5,60,0.5,1.3,0.2,0.01)
x2, y2 = p2.evolve_runge_kutta()

plt.plot(x1,y1, label = "Euler")
plt.plot(x2,y2, label = "Runge-kutta")
plt.legend()
plt.show()