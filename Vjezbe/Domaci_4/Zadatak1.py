import Projectile as pro
import numpy as np
import math

p1 = pro.Projectile()
p1.set_initial_conditions(0,0,10,10,50,1.3,0.2,0.01,2,"kugla")
p1.evolve_runge_kutta()

p1.reset()
p1.set_initial_conditions(0,0,10,10,50,1.3,0.2,0.01,2,"kocka")
p1.evolve_runge_kutta()