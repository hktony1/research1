import pickle
import numpy as np
import matplotlib.pyplot as plt


file = 'orbits_prelim.pkl'

with open(file,'rb') as f:
    data = pickle.load(f)

yay = data['data']


time = yay[0]['Time']
mass = yay[0]['mass']

plt.plot(time,mass)
plt.xlabel('time (strange units, TBD)')
plt.yscale("log")
plt.ylabel('mass (Msun)')
plt.show()
