import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt 
#empty list to append stuff into
x=[]
y=[]
z=[]
#how to load multiple snapshots(p.list is a file with a lot of snapshots)
snapshots=np.loadtxt('p.list',dtype=np.str)
for i in range(len(snapshots)):
    s=pynbody.load(snapshots[i])
    s.physical_units()
    halos=s.halos()
    #t=s.properties['time'].in_units('Gyr')[i]
    #i commented this out because it wouldn't work sometimes
    #how to find which halo a black hole is in using iord number
    def findBH(s):
        iord=s.stars['iord']
        BHfilter = np.where(iord==60354588)
        BH = s.stars[BHfilter]
        return BH
    def findBHhalos(s):
        BH = findBH(s)
        BHhalos = BH['amiga.grp']
        return BHhalos
    BHhalos = findBHhalos(s)
    idx=BHhalos
    halo=halos[idx]
    print(halo)
    if idx==0:
        continue
    #this gives us the center postion of the halo the black hole is in
    center=pynbody.analysis.halo.center(halo,mode='hyb',retcen=True)
    #appending is just taking the data the previous line go and putting them into an empty list to use for later
    x.append(center[0])
    y.append(center[1])
    z.append(center[2])
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x (kpc)')
ax.set_ylabel('y (kpc)')
ax.set_zlabel('z (kpc)')
ax.plot3D(x,y,z)
plt.show()