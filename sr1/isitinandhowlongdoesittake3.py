import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
import gc
snapshots=np.loadtxt('elena.list',dtype=np.str)
def findmainBH(s):
    mainiord=s.stars['iord']
    mainBHfilter = np.where(mainiord==40810270)
    mainBH = s.stars[mainBHfilter]
    return mainBH
def findmainBHhalos(s):
    mainBH = findmainBH(s)
    mainBHhalos = mainBH['amiga.grp']
    return mainBHhalos

def findmergingBH(s):
    mergingiord=s.stars['iord']
    mergingBHfilter = np.where(mergingiord==40810454)
    mergingBH = s.stars[mergingBHfilter]
    return mergingBH
def findmergingBHradius(s):
    mergingBH=findmergingBH(s)
    mergingBHradius=mergingBH['r']
    return mergingBHradius

def findmergingBH2(s):
    mergingiord2=s.stars['iord']
    mergingBHfilter2 = np.where(mergingiord2==40811872)
    mergingBH2 = s.stars[mergingBHfilter2]
    return mergingBH2
def findmergingBHradius2(s):
    mergingBH2=findmergingBH2(s)
    mergingBHradius2=mergingBH2['r']
    return mergingBHradius2

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
    print("The merging black hole 40810454 is this distance from the center",mergingBHradius)
    print("The merging black hole 40811872 is this distance from the center",mergingBHradius2)
    MA.append(mergingBHradius)
    del(s)
    del(halos)
    gc.collect()