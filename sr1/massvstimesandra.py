import pickle
import matplotlib.pyplot as plt 
import numpy as np 
#as thwe title would imply how to load a pickle
file="sandra.orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
iord=data['iord']
for i in range(len(yay)):
    plt.plot(yay[i]['Time'].in_units('Gyr'),np.log10(yay[i]['mass']),label=iord[i])
plt.legend(bbox_to_anchor=(1,1.15))
plt.xlabel('Time (Gyr)',fontsize=20)
plt.ylabel('Log Mass ($M_{\odot}$)',fontsize=20)
plt.title('Mass vs Time For All Black Holes in Sandra', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()