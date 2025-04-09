import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = x
y2 = 2 * x
y3 = 3 * x
y4 = x**2
y5 = 2*x**2
plt.plot(x, y1, color='black')   
plt.plot(x, y2, color='red')  
plt.plot(x, y3, color='blue')  
plt.plot(x, y4, color='green')  
plt.plot(x, y5, color='pink')  
plt.show()