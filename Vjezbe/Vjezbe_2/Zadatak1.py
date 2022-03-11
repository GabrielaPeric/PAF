import numpy as np 
a = 0 
v = 0
x = 0
v0 = 0
x0 = 0
F = 100
m = 5
t = np.arange(0,10,1)
for i in np.arange(0,10,1):
    a = F/m 
    v = v0 + a*t
    x  = x0 + v0*t + 1/2*a*t**2
print(a)
print(v)
print(x)
