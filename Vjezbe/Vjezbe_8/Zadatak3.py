from tables import restrict_flavors
import Projectile
import matplotlib.pyplot as plt
import math 
import numpy as np 

def ovisnost_dometa_o_Cd():
    #Domet_lista_Euler = []
    Domet_lista_runge_kutta = []
    #Domet_Euler = 0
    Domet_Runge_kutta = 0
    
    Cd_arange = np.arange(0,50.1,0.1)
    Cd_lista = Cd_arange.tolist()

    p1 = Projectile.Projectile()

    for i in Cd_lista:
        p1.set_initial_conditions(0,0,20,5,30,0.5,1.3,i,0.01)
        Domet_Runge_kutta = p1.domet_runge_kutta()
        Domet_lista_runge_kutta.append(Domet_Runge_kutta)
        p1.reset()

    plt.plot(Cd_lista,Domet_lista_runge_kutta)
    plt.show()


def ovisnost_dometa_o_m():
    Domet_Runge_kutta = 0
    Domet_lista_runge_kutta = []

    m_arange = np.arange(0.1,10.1,0.1)
    m_lista = m_arange.tolist()

    p2 = Projectile.Projectile()

    for el in m_lista:
        p2.set_initial_conditions(0,0,10,el,30,0.5,1.3,2,0.01)
        Domet_Runge_kutta = p2.domet_runge_kutta()
        Domet_lista_runge_kutta.append(Domet_Runge_kutta)
        p2.reset()

    plt.plot(m_lista, Domet_lista_runge_kutta)
    plt.show()

ovisnost_dometa_o_Cd()
ovisnost_dometa_o_m()









