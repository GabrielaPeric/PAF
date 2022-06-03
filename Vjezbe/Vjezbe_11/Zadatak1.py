import Gravity
import matplotlib.pyplot as plt 

p1 = Gravity.Gravity()
p1.set_initial_conditions()
p1.Evolve()

plt.plot(p1.x_sun_lista, p1.y_sun_lista, p1.x_earth_lista, p1.y_earth_lista)
plt.show()