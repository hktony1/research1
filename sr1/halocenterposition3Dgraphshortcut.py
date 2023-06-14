import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt 
#after apending data and saving it into an numpy array i can load the files up with the data and just graph it
x=np.load('xposition.npy')
y=np.load('yposition.npy')
z=np.load('zposition.npy')
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x (kpc)')
ax.set_ylabel('y (kpc)')
ax.set_zlabel('z (kpc)')
ax.plot3D(x,y,z)
plt.show()