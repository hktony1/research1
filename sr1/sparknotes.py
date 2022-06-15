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
    plt.plot(yay[i]['Time'],yay[i]['mass'],label='bh'[i])
    plt.xlabel('Time (?)')
    plt.ylabel('Mass (Msol)')
        
    
    
