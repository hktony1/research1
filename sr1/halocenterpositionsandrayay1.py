import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt 
x=[]
y=[]
z=[]
time=[]
def findBH(s):
    iord=s.stars['iord']
    BHfilter = np.where(iord==75288505)
    BH = s.stars[BHfilter]
    return BH
def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos
snapshots=np.loadtxt('sonia.list',dtype=np.str)
for i in range(len(snapshots)):
    s=pynbody.load(snapshots[i])
    s.physical_units()
    halos=s.halos()
    t=s.properties['time'].in_units('Gyr')
    BHhalos = findBHhalos(s)
    print("halo is", BHhalos)
    print("time is", t)
    idx=BHhalos
    halo=halos[idx]
    if idx==0:
        continue
    center=pynbody.analysis.halo.center(halo,mode='hyb',retcen=True)
    print("center is", center)
    x.append(center[0])
    y.append(center[1])
    z.append(center[2])
    time.append(t)
np.save(soniax,x)
np.save(soniay,y)
np.save(soniaz,z)