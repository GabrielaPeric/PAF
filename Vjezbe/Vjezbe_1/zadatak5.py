import matplotlib.pyplot as plt
import numpy as np

def crtanje(x1,y1,x2,y2):
    k = (y2 -y1)/(x2-x1)
    l = y1 - k*x1
    
    x = np.arange(0,10,1)
    x_lista = x.tolist()
    y_lista = []
    
    for i in x_lista:
        y_lista.append( k * i + l)

    plt.scatter([x1,x2],[y1,y2], color='gray')

    plt.plot(x,y_lista,linestyle='-')

    plt.xlabel('x',fontsize=8)
    plt.ylabel('y',fontsize=8)
    

    plt.grid()

    plt.show()
    
a = crtanje(1,2,3,4)