import numpy as np
import matplotlib.pyplot as plt 
redshift = np.loadtxt("times.list")[:,0]
time = np.loadtxt("times.list")[:,1]

plt.plot(redshift, time)
plt.xlabel('redshift ()')
plt.ylabel('time (Gigayear)')

plt.show()