import pickle
import matplotlib.pyplot as plt 
import numpy as np 
file="sandra.acclog.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
Mgas=yay[0]['deltaMgas']
cuMgas = np.cumsum(Mgas)
time=yay[0]['time']
Mbh=yay[0]['Mbh']
cuMbh = np.cumsum(Mbh)
ratio=cuMgas/Mbh
plt.ylabel('Accreted gas/Total mass (Solar Mass)',fontsize=15)
plt.xlabel('Time (GYrs)',fontsize=15)
plt.title('Percentage of Accretion at Any Given Time',fontsize=20)
newtime=time>0.34
plt.plot(time[newtime],ratio[newtime])
plt.show()