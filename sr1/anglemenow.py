import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
import gc
file='/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.000275/h148.cosmo50PLK.3072g3HbwK1BH.000275'
def findmainBH(s):
    mainiord=s.stars['iord']
    mainBHfilter = np.where(mainiord==101863510)
    mainBH = s.stars[mainBHfilter]
    return mainBH
def findmainBHhalos(s):
    mainBH = findmainBH(s)
    mainBHhalos = mainBH['amiga.grp']
    return mainBHhalos
def findmergingBH(s):
    mergingiord=s.stars['iord']
    mergingBHfilter = np.where(mergingiord==101863741)
    mergingBH = s.stars[mergingBHfilter]
    return mergingBH
s=pynbody.load(file)
s.physical_units()
h=s.halos()
mainBHhalos=findmainBHhalos(s)
idx=mainBHhalos
main=h[idx]
mergingBH=findmergingBH(s)
pynbody.analysis.angmom.sideon(main)
position=mergingBH['pos']
velocity=mergingBH['vel']
angmom=pynbody.analysis.angmom.ang_mom_vec(main)
c=np.cross(position,velocity)
dot=np.dot(c,angmom)
normc=np.linalg.norm(c)
normangmom=np.linalg.norm(angmom)
angle=np.arccos(dot/(normc*normangmom))
print(angle)