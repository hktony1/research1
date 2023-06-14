#how to load a snapshot using pynbody
import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt 
file='/mnt/data0/jillian/h329/h329.cosmo50PLK.3072gst5HbwK1BH.000637/h329.cosmo50PLK.3072gst5HbwK1BH.000637'
snap=pynbody.load(file)
snap.physical_units()
snap.families()
halos=snap.halos()
time=pynbody.analysis.cosmology.age(snap,unit='Gyr')
print(time)
#this function only takes tform values lower than 0 because black holes tform value are all negative
def findBH(snap):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = snap.stars[BHfilter]
    return BH
#uses iord number to find halo
def findBHhalos(snap):
    BH = findBH(snap)
    BHhalos = BH['amiga.grp']
    return BHhalos
def iordfindBHhalos(snap):
    BHhalos = findBHhalos(snap)
    BH = findBH(snap)
    iordfilter = np.where(BH['iord']==75288505)
    answer = BHhalos[iordfilter]
    return answer
answer=iordfindBHhalos(snap)
print(answer)