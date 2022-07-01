import pickle
import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits import mplot3d
file="orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
x=yay[0]['x']
y=yay[0]['y']
z=yay[0]['z']
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x,y,z)
file2="acclog.pkl"
with open(file2,'rb') as f:
    data=pickle.load(f)
yay2=data['data']
dx