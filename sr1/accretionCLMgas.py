import pickle
import matplotlib.pyplot as plt 
import numpy as np 
#this is how to load a pickle file
file="acclog.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
#i call all my data in pickle files yay
#this is just a graph of the total mass gained by accretion
yay=data['data']
deltaMgas=yay[0]['deltaMgas']
time=yay[0]['time']
cumulative = np.cumsum(deltaMgas)
cumlog=np.log10(cumulative)
plt.plot(time,cumlog)
plt.ylabel('Gas Accreted (Solar Mass)',fontsize=15)
plt.xlabel('Time (Gyrs)',fontsize=15)
plt.title('Cumulative Gas Accretion',fontsize=20)
plt.show()
