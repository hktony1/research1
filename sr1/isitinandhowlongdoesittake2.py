import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
import gc
snapshots=np.loadtxt('sonia.list',dtype=np.str)
def findmainBH(s):
    mainiord=s.stars['iord']
    mainBHfilter = np.where(mainiord==75288505)
    mainBH = s.stars[mainBHfilter]
    return mainBH
def findmainBHhalos(s):
    mainBH = findmainBH(s)
    mainBHhalos = mainBH['amiga.grp']
    return mainBHhalos

def findmergingBH(s):
    mergingiord=s.stars['iord']
    mergingBHfilter = np.where(mergingiord==75289316)
    mergingBH = s.stars[mergingBHfilter]
    return mergingBH
def findmergingBHradius(s):
    mergingBH=findmergingBH(s)
    mergingBHradius=mergingBH['r']
    return mergingBHradius

def findmergingBH2(s):
    mergingiord2=s.stars['iord']
    mergingBHfilter2 = np.where(mergingiord2==75288553)
    mergingBH2 = s.stars[mergingBHfilter2]
    return mergingBH2
def findmergingBHradius2(s):
    mergingBH2=findmergingBH2(s)
    mergingBHradius2=mergingBH2['r']
    return mergingBHradius2

def findmergingBH3(s):
    mergingiord3=s.stars['iord']
    mergingBHfilter3 = np.where(mergingiord3==75288614)
    mergingBH3 = s.stars[mergingBHfilter3]
    return mergingBH3
def findmergingBHradius3(s):
    mergingBH3=findmergingBH3(s)
    mergingBHradius3=mergingBH3['r']
    return mergingBHradius3
def findmergingBH4(s):
    mergingiord4=s.stars['iord']
    mergingBHfilter4 = np.where(mergingiord4==75289109)
    mergingBH4 = s.stars[mergingBHfilter4]
    return mergingBH4
def findmergingBHradius4(s):
    mergingBH4=findmergingBH4(s)
    mergingBHradius4=mergingBH4['r']
    return mergingBHradius4
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
    mergingBHradius4=findmergingBHradius4(s)
    print("The merging black hole 75289316 is this distance from the center",mergingBHradius)
    print("The merging black hole 75288553 is this distance from the center",mergingBHradius2)
    print("The merging black hole 75288614 is this distance from the center",mergingBHradius3)
    print("The merging black hole 75289109 is this distance from the center",mergingBHradius4)
    MA.append(mergingBHradius)
    del(s)
    del(halos)
    gc.collect()