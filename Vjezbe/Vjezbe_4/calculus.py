import math
import matplotlib.pyplot as plt
import numpy as np

def derivacija_two_point(func, x):
    h = 0.1 #Ovo je korak
    return (func(x+h)-func(x))/h

def derivacija_three_point(func, x):
    h = 0.1
    return (func(x+h)-func(x-h))/(2*h)    

def derivacija(func,a,b,metoda):
    h = 0.1
    x_lista = []
    y_lista = []
    
    while a <= b:  #dok je donja granica manja od gornje u x listu unosi x koordinate 
        x_lista.append(a)
        a += h
    
    if metoda == 2:  #ako korisnik odabere 2, to znaci da zeli 2-point metodu
        for element in x_lista:
            derivacija = derivacija_two_point(func,element)
            y_lista.append(derivacija)
    
    elif metoda == 3: #ako korisnik odabere 3, to znaci da zeli 3-point metodu
        for element in x_lista:
            derivacija = derivacija_three_point(func,element)
            y_lista.append(derivacija)
       

    return plt.scatter(x_lista,y_lista), x_lista, y_lista


#def integral_pravokutnik(func,a,b,n):
    dx = (b-a)/n 
    gornja_meda = 0
    donja_meda = 0
    c = a + dx    #za gornju medu pocinjemo od x1
    d = a    #za donju medu pocinjemo od x0
    for i in range(n):
        gornja_meda += func(c)*dx
        c += dx
        donja_meda += func(d)*dx
        d += dx
    return gornja_meda, donja_meda

#def integral_trapez(func,a,b,n):
    dx = (b-a)/n
    zbroj = 0
    

    

