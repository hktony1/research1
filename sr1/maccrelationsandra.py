import pickle
import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits import mplot3d
#MACC RELATION FOR ONLY SANDRA
file="sandra.orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
file2='sandra.acclog.pkl'
with open(file2,'rb') as f:
    data2=pickle.load(f)
yay2=data2['data']
mass=[]
ratio=[]
for i in range(len(yay)):
    yay[i]['mass'][-1]
    if yay[i]['mass'][-1]>1000:
        mass.append(yay[i]['mass'][-1])
        
for j in range(len(yay2)):
    Mgas=yay2[j]['deltaMgas']
    cuMgas=np.cumsum(Mgas)[-1]
    Mbh=yay2[j]['Mbh'][-1]
    ratio2=cuMgas/Mbh
    if yay2[j]['Mbh'][-1]>1000:
        ratio.append(ratio2)
        
plt.scatter(mass,ratio)
plt.ylabel('Accretion percentage at z=0')
plt.xlabel('Final Mass (Msol)')
plt.show()