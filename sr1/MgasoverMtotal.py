import pickle
import matplotlib.pyplot as plt 
import numpy as np 
#how to load a pickle file
file="acclog.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
# graph of Percentage of Mass Accreted at any Given Time
yay=data['data']
Mgas=yay[0]['deltaMgas']
cuMgas = np.cumsum(Mgas)
time=yay[0]['time']
Mbh=yay[0]['Mbh']
cuMbh = np.cumsum(Mbh)
ratio=cuMgas/Mbh
nratio=ratio*100
plt.ylabel('Gas Accreted/Total Mass(%)', fontsize=20)
plt.xlabel('Time (Gyr)',fontsize=20)
plt.title('Percentage of Mass Accreted at any Given Time',fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
newtime=time>0.34
plt.plot(time[newtime],nratio[newtime])
plt.show()