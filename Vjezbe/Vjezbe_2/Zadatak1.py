import numpy as np 
import matplotlib.pyplot as plt

F = 100 #Unesite silu u Njutinima 
m = 10 #Unesite masu čestice u kilogramima
t = np.arange(0.0, 10.5, 0.5) #za prvih deset sekundi 
t_list = t.tolist()
x = [0]
v = [0]
a = [10] #akcelercija je konstantna 
interval = 0.5

for i in range(len(t_list) -1 ): #imamo unesene u listu vec pocetne vrijednosti pa for petlja treba imat ponavljanja len(broj intervala)-1
    a.append(F/m)
    v.append(v[i]+a[i]*interval)
    x.append(x[i]+v[i+1]*interval)

print(t_list)
print(a)
print(v)
print(x)

figure, axis = plt.subplots(1, 3)
axis[0].plot(t,a)
axis[1].plot(t, v)
axis[2].plot(t, x)
plt.show()


