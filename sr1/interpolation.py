import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
file="orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
x=np.load('xposition.npy')
y=np.load('yposition.npy')
z=np.load('zposition.npy')
yay=data['data']
time=yay[0]['Time']
x0=yay[0]['x']
y0=yay[0]['y']
z0=yay[0]['z']
xi=np.interp(x0,x,x)
yi=np.interp(x0,x,y)
zi=np.interp(x0,x,z)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x,y,z,'red')
ax.plot3D(xi,yi,zi,'blue')
plt.show()
