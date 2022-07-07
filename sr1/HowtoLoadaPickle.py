import pickle
import matplotlib.pyplot as plt 
import numpy as np 
file="orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
time=yay[0]['Time']
mass=yay[0]['mass']
for i in range(len(yay)):
    plt.plot(yay[i]['Time'],np.log10(yay[i]['mass']))
plt.ylabel('Log10 Mass (Msol)')
plt.xlabel('Time')
plt.show()