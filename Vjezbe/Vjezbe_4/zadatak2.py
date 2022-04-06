import matplotlib.pyplot as plt
import math
import calculus as cal

def funkcija_1(x):
    return(x**3+5*x**2+3)

def funkcija_1_integirirana(x):
    return ((x**4/4)+(5*x**3/3)+3*x)

#print(cal.integral_pravokutnik(funkcija_1,0,5,50))
#print(cal.integral_trapez(funkcija_1,0,5,50))

a = 0
b = 5
dn = 10
nlista = []
g_mede = []
d_mede = []
analitic = []
trapez = []

for i in range(1,20):
    nlista.append(dn*i)

for n in nlista:
    gornja, donja = cal.integral_pravokutnik(funkcija_1,a,b,n)
    g_mede.append(gornja)
    d_mede.append(donja)
    integral_t = cal.integral_trapez(funkcija_1,a,b,n)
    trapez.append(integral_t)
    integral_a = funkcija_1_integirirana(b) - funkcija_1_integirirana(a)
    analitic.append(integral_a)

plt.scatter(nlista,g_mede)
plt.scatter(nlista,d_mede)
plt.scatter(nlista,trapez)
plt.plot(nlista,analitic)
plt.show()

