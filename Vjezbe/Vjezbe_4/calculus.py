def derivacija_two_point(func, x):
    h = 0.1 #Ovo je korak
    return (func(x+h)-func(x))/h

def derivacija_three_point(func, x):
    h = 0.1
    return (func(x+h)-func(x-h))/(2*h)    

def derivacija_s_rasponom(func,x,a,b): #func je funckija, x je tocka u funkciji, a i be su međe
    x_lista = [x]
    while x_lista[-1] <= b:
        
