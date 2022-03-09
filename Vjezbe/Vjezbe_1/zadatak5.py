import matplotlib.pyplot as plt
import numpy as np

x1 = 2.0
y1 = 3.0

x2 = 6.0
y2 = 5.0

a = (y2 - y1) / (x2 - x1)
b = y1 - a * x1

x = np.linspace(0, 8, 100)
y = a * x + b

plt.scatter([x1,x2],[y1,y2], color='gray')

plt.plot(x,y,linestyle='-')

plt.xlabel('x',fontsize=8)
plt.ylabel('y',fontsize=8)

plt.xlim(0,8)
plt.ylim(0,8)

plt.grid()

plt.savefig("calculate_line_slope_and_intercept.pdf")
plt.show()