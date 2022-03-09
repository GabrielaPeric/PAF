x1 = int(input("Unesite x koordinatu prve tocke: "))
y1 = int(input("Unesite y koordinatu prve tocke: "))
x2 = int(input("Unesite x koordinatu druge tocke: "))
y2 = int(input("Unesite y koordinatu druge tocke: "))
k = 0
l = 0
def nagib_odsjecak():
    k = (y2-y1)/(x2-x1)
    l = y1 - k * x1 
    return k,l
a = nagib_odsjecak()
print(a)
print("y = {}x + {}".format(a[0],a[1]))
