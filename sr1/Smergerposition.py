import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
file="sandra.orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
x=np.load('sandraxpos.npy')
y=np.load('sandraypos.npy')
z=np.load('sandrazpos.npy')
sandratime=np.load('sandratime.npy')
yay=data['data']
time=yay[1]['Time']
timeg=time.in_units('Gyr')
x1=yay[1]['x']
y1=yay[1]['y']
z1=yay[1]['z']
xi=np.interp(timeg,sandratime,x)
yi=np.interp(timeg,sandratime,y)
zi=np.interp(timeg,sandratime,z)
"""N=len(x1)
xi=np.zeros(N)
yi=np.zeros(N)
zi=np.zeros(N)
for i in range(len(x)-1):
    xstep=[x[i],x[i+1]]
    ystep=[y[i],y[i+1]]
    zstep=[z[i],z[i+1]]
    keep=np.logical_and(x1>x[i],x1<x[i+1])
    xi[keep]=np.interp(x1[keep],xstep,xstep)
    yi[keep]=np.interp(x1[keep],xstep,ystep)
    zi[keep]=np.interp(x1[keep],xstep,zstep)"""
x4=yay[4]['x']
y4=yay[4]['y']
z4=yay[4]['z']
xc=xi[300512:1163486]
yc=yi[300512:1163486]
zc=zi[300512:1163486]
x4new=x4[300000:1162974]
y4new=y4[300000:1162974]
z4new=z4[300000:1162974]
newx=x4new-xc
newy=y4new-yc
newz=z4new-zc
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title("Sm1")
#ax.plot3D(newx,newy,newz)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot3D(xc,yc,zc)
ax.plot3D(x4new,y4new,z4new)
plt.show()