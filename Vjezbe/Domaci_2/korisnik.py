import Zadatak1 as m
def f1(v,x,t):
    return 10

def f2(v,x,t):
    k = 10
    return -k*x
    
p1 = m.Gibanje()
p1.set_initial_conditions(f1,0,5,5,0.1)
p1.print()

p2 = m.Gibanje()
p2.set_initial_conditions(f2,0,5,5,0.1)
p2.print()

