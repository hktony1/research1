import pickle
import matplotlib.pyplot as plt 
import numpy as np 
file="orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
time=yay[0]['Time']
mass=yay[0]['mass']
for i in range(len(yay[0])):
    plt.plot(yay[i]['Time'].in_units('Gyr'),np.log10(yay[i]['mass']))
plt.xlabel('Time (Gyr)',fontsize=20)
plt.ylabel('Log Mass ($M_{\odot}$)',fontsize=20)
plt.title('Mass vs Time For All 45 Black Holes in Ruth', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()
        
    
    
