def jednoliko_gibanje(F,m):
    import numpy as np 
    import matplotlib.pyplot as plt

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

    figure, axis = plt.subplots(1, 3)

    axis[0].set_title("a-t graf")
    axis[1].set_title("v-t graf")
    axis[2].set_title("x-t graf")

    axis[0].plot(t,a)
    axis[1].plot(t, v)
    axis[2].plot(t, x)

    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
    plt.show()



def kosi_hitac(v0, theta):
    import numpy as np 
    import math 
    import matplotlib.pyplot as plt 

    v0_x = v0*math.cos((theta/360)*2*math.pi)
    v0_y = v0*math.sin((theta/360)*2*math.pi)
    t = np.arange(0.0, 10.5, 0.5) #za prvih deset sekundi 
    t_list = t.tolist()
    x = [0]
    y = [0]
    v_x = [v0_x] #brzina je konstantna u x smjeru
    v_y = [v0_y]
    a_x = [0] #brzina konstanta pa nema akceleracije
    a_y = [9.81] #ovo je g akceleracija, slobodni pad, akceleracija je konstanta
    interval = 0.5

    for i in range(len(t_list) -1 ):
        a_x.append(0)
        a_y.append(9.81)
        v_x.append(v0_x)
        v_y.append(v_y[i]-a_y[i]*interval)
        x.append(x[i]+v_x[i+1]*interval)
        y.append(y[i]+v_y[i+1]*interval)

    figure, axis = plt.subplots(1, 3)
    axis[0].set_title("x-y graf")
    axis[1].set_title("x-t graf")
    axis[2].set_title("y-t graf")

    axis[0].set_ylabel('y(m)')
    axis[0].set_xlabel('x(m)')

    axis[1].set_ylabel('t(s)')
    axis[1].set_xlabel('x(m)')

    axis[2].set_ylabel('t(s)')
    axis[2].set_xlabel('y(m)')


    axis[0].plot(x,y)
    axis[1].plot(t, x)
    axis[2].plot(t, y)

    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
    plt.show()