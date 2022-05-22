import Projectile as pro
import math
import numpy as np
import matplotlib.pyplot as plt

a = pro.Projectile()
#a.set_initial_conditions(0,0,10,10,50,1.3,0.2,0.01,2,"kugla")
#a.angle_to_hit_the_target(2,4,2)

#a.reset()


a.set_initial_conditions(0,0,10,10,10,1.3,0.2,0.01,2,"kugla")
a.evolve_runge_kutta()
plt.plot(a.x, a.y)

a.reset()
a.set_initial_conditions(0,0,10,10,50,1.3,0.2,0.01,2,"kugla")
a.evolve_runge_kutta()
plt.plot(a.x,a.y)

a.reset()
a.set_initial_conditions(0,0,10,10,88,1.3,0.2,0.01,2,"kugla")
a.evolve_runge_kutta()
plt.plot(a.x,a.y)

a.reset()

meta = [[4,2,2]]
for i in meta:
    plt.plot(i[0], i[1], marker = 'o', markersize = i[2])

plt.show()


