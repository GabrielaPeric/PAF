import EmField
import numpy as np
import matplotlib.pyplot as plt

def Konstantni_B(t):
    return np.array((0,0,1))

def Promjenjivo_B(t):
    return np.array((0,0,t/10))

p1 = EmField.EmField()
p1.set_initial_conditions(1,-1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]), Konstantni_B)
p1.evolve_runge_kutta(10)

p2 = EmField.EmField()
p2.set_initial_conditions(1,-1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]), Promjenjivo_B)
p2.evolve_runge_kutta(10)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.plot(p1.x_lista,p1.y_lista,p1.z_lista)
ax.plot(p2.x_lista,p2.y_lista,p2.z_lista)

plt.show()

p1.reset()
p2.reset()

p1 = EmField.EmField()
p1.set_initial_conditions(1,-1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]), Promjenjivo_B)
p1.evolve_runge_kutta(10)

p2 = EmField.EmField()
p2.set_initial_conditions(1,1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]), Promjenjivo_B)
p2.evolve_runge_kutta(10)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.plot(p1.x_lista,p1.y_lista,p1.z_lista)
ax.plot(p2.x_lista,p2.y_lista,p2.z_lista)

plt.show()