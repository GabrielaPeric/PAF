import math
import matplotlib.pyplot as plt
import HarmonicOscillator as ho

h1 = ho.HarmonicOscillator()
h1.set_initial_conditions(0,10,4,5,0.5)
h1.oscillate(10)




h2 = ho.HarmonicOscillator()
h2.set_initial_conditions(0,10,4,5,0.01)
h2.oscillate(10)




h3 = ho.HarmonicOscillator()
h3.set_initial_conditions(0,10,4,5,0.1)
h3.oscillate(10)




def graf():
    plt.scatter(h1.t,h1.x, color = "green")
    plt.scatter(h2.t,h2.x, color = "red")
    plt.scatter(h3.t,h3.x, color = "blue")

    plt.show()

graf()

h1.period()
h2.period()
h3.period()
h1.period_analitic()