x1 = int(input("Unesite x koordinatu prve tocke: "))
y1 = int(input("Unesite y koordinatu prve tocke: "))
x2 = int(input("Unesite x koordinatu druge tocke: "))
y2 = int(input("Unesite y koordinatu druge tocke: "))
k = (y2-y1)/(x2-x1)
l = y1 - k * x1 
print(k)
print(l)
print("y = {}x + {}" .format(k,l))   