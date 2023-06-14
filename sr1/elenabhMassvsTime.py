import pickle
import matplotlib.pyplot as plt 
import numpy as np 
#plot for all black holes mass vs time in sandra
file="elena.orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
time=yay[0]['Time']
mass=yay[0]['mass']
iord=data['iord']
for i in range(len(yay)):
    plt.plot(yay[i]['Time'].in_units('Gyr'),np.log10(yay[i]['mass']),label=iord[i])
plt.ylabel('Log10 Mass (Msol)')
plt.xlabel('Time')
plt.legend(bbox_to_anchor=(1,1.15))
plt.title('Mass vs Time')
plt.show()