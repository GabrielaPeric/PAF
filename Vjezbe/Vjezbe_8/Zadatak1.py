import matplotlib.pyplot as plt 
import Projectile 

p = Projectile.Projectile()
p.set_initial_conditions(0,0,10,5,60,0.5,1.3,0.2,0.01)
p.evolve_Euler()

plt.plot(p.x,p.y)
plt.show()