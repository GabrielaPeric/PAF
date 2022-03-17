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
jednoliko_gibanje(100,10)
