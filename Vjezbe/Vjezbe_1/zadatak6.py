import math
radijus = 3
xr = int(input("Unesite x koordinatu sredista kruznice: "))
yr = int(input("Unesite y koordinatu sredista kruznice: "))
a = int(input("Unesite x koordinatu tocke: "))
b = int(input("Unesite y koordinatu tocke: "))
udaljenost = 0 
zakljucak = "."
def udaljenost_izmedju_dvije_tocke():
    udaljenost = math.sqrt((a-xr)**2+(b-yr)**2)
    if udaljenost < radijus:
        zakljucak = "Tocka se nalazi unutar kruznice."
    elif udaljenost == radijus:
        zakljucak = "Tocka se nalazi na kruznici."
    else:
        zakljucak = "Tocka se nalazi izvan kruznice."
    return zakljucak
print(udaljenost_izmedju_dvije_tocke())

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)

r = np.sqrt(3.0)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

fig, ax = plt.subplots(1)

ax.plot(x1, x2)
ax.set_aspect(1)

plt.xlim(-4.25,4.25)
plt.ylim(-4.25,4.25)

plt.grid(linestyle='--')

plt.plot(a,b,'ro') 

plt.plot(xr,yr,'ro')

plt.show()