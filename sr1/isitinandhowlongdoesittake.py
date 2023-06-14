import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
import gc
snapshots=np.loadtxt('p.list',dtype=np.str)
def findmainBH(s):
    mainiord=s.stars['iord']
    mainBHfilter = np.where(mainiord==60352780)
    mainBH = s.stars[mainBHfilter]
    return mainBH
def findmainBHhalos(s):
    mainBH = findmainBH(s)
    mainBHhalos = mainBH['amiga.grp']
    return mainBHhalos

def findmergingBH(s):
    mergingiord=s.stars['iord']
    mergingBHfilter = np.where(mergingiord==60352867)
    mergingBH = s.stars[mergingBHfilter]
    return mergingBH
def findmergingBHradius(s):
    mergingBH=findmergingBH(s)
    mergingBHradius=mergingBH['r']
    return mergingBHradius

def findmergingBH2(s):
    mergingiord2=s.stars['iord']
    mergingBHfilter2 = np.where(mergingiord2==60353760)
    mergingBH2 = s.stars[mergingBHfilter2]
    return mergingBH2
def findmergingBHradius2(s):
    mergingBH2=findmergingBH2(s)
    mergingBHradius2=mergingBH2['r']
    return mergingBHradius2

def findmergingBH3(s):
    mergingiord3=s.stars['iord']
    mergingBHfilter3 = np.where(mergingiord3==60352912)
    mergingBH3 = s.stars[mergingBHfilter3]
    return mergingBH3
def findmergingBHradius3(s):
    mergingBH3=findmergingBH3(s)
    mergingBHradius3=mergingBH3['r']
    return mergingBHradius3
SA=[]
HA=[]
VA=[]
MA=[]
for i in range(len(snapshots)):
    s=pynbody.load(snapshots[i])
    print("This is snapshot",s[i])
    SA.append(snapshots[i])
    s.physical_units()
    halos=s.halos()
    mainBHhalos=findmainBHhalos(s)
    idx=mainBHhalos
    print("The main black hole is in halo",idx)
    HA.append(idx)
    if idx==0:
        continue
    main=halos[idx]
    pynbody.analysis.angmom.sideon(main)
    vr=pynbody.analysis.halo.virial_radius(main)
    print("The virial radius is",vr)
    VA.append(vr)
    mergingBHradius=findmergingBHradius(s)
    mergingBHradius2=findmergingBHradius2(s)
    mergingBHradius3=findmergingBHradius3(s)
    print("The merging black hole 60352867 is this distance from the center",mergingBHradius)
    print("The merging black hole 60353760 is this distance from the center",mergingBHradius2)
    print("The merging black hole 60352912 is this distance from the center",mergingBHradius3)
    MA.append(mergingBHradius)
    del(s)
    del(halos)
    gc.collect()
    
np.savetxt("/home/hktony1/research1/sr1/megeringof0_8.txt", np.c_[SA,HA,VA,MA])