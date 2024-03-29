import pickle
import matplotlib.pyplot as plt 
import numpy as np 
file="sandra.acclog.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
deltaMgas=yay[1]['deltaMgas']
time=yay[1]['time']
cumulative = np.cumsum(deltaMgas)
cumlog=np.log10(cumulative)
plt.plot(time,cumlog)
plt.ylabel('Mgas (Msol)')
plt.xlabel('Time (Gyrs)')
#plt.arrow(2.5,5.5,0.5,0,width=0.04,length_includes_head=True,)
#plt.text(0,5.5,'Total Mgas \n accreted',fontsize=9)
plt.show()