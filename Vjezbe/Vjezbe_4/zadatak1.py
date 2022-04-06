import calculus as cal
import math 
import matplotlib.pyplot as plt 
import numpy as np

def funckija_1(x):
    return(x**3+5*x**2+3)

def funkcija_2(x):
    return(np.sin(x)+2)    

def funkcija_1_derivirana(x):
    return(3*x**2+10*x)

def funkcija_2_derivirana(x):
    return(np.cos(x))


#print(cal.derivacija_two_point(funckija_1,2))
#print(cal.derivacija_three_point(funckija_1,2))

lista_za_x1 = np.arange(0,2.1,0.1)
lista_za_y1 = funkcija_1_derivirana(lista_za_x1)


def slika_za_funkciju_1():
    cal.derivacija(funckija_1,0,2,3)
    plt.plot(lista_za_x1,lista_za_y1)
    plt.show()


slika_1 = slika_za_funkciju_1()
slika_1

lista_za_x2 = np.arange(0,10,0.1)
lista_za_y2 = funkcija_2_derivirana(lista_za_x2)


def slika_za_funkciju_2():
    cal.derivacija(funkcija_2,0,10,3)
    plt.plot(lista_za_x2,lista_za_y2)
    plt.show()

slika2 = slika_za_funkciju_2()
slika2

#print((cal.derivacija(funckija_1,0,2,3)))
#print((cal.derivacija(funkcija_2,0,10,3)))






