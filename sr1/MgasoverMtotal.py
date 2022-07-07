import pickle
import matplotlib.pyplot as plt 
import numpy as np 
file="acclog.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
Mgas=yay[0]['deltaMgas']
cuMgas = np.cumsum(Mgas)
time=yay[0]['time']
Mbh=yay[0]['Mbh']
cuMbh = np.cumsum(Mbh)
ratio=cuMgas/Mbh
plt.ylabel('Cumulative Mgas/Mtotal')
plt.xlabel('Time (GYrs)')
newtime=time>0.34
plt.plot(time[newtime],ratio[newtime])
plt.show()