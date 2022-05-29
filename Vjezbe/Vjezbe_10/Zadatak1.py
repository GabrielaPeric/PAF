import EMField
import numpy as np
import matplotlib.pyplot as plt 

p1 = EMField.EmField()
p1.set_initial_conditions(1,-1,np.array((0,0,0)),np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,1)))
p1.evolve_euler(20)

p2 = EMField.EmField()
p2.set_initial_conditions(1,1,np.array((0,0,0)),np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,1)))
p2.evolve_euler(20)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.plot(p1.x_lista,p1.y_lista,p1.z_lista)
ax.plot(p2.x_lista,p2.y_lista,p2.z_lista)

plt.show()