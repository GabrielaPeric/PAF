import matplotlib.pyplot as plt 
import ProjectileDrop as pd 

p3 = pd.ProjectileDrop()
p3.__init__()
p3.set_initial_conditions(10,5)
p3.promjena_visine(2000)
p3.promjena_brzine(200)
p3.kretanje()
p3.grafovi()