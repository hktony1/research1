import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt 
#how to load a snapshot using pynbody
file='/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.004096/h148.cosmo50PLK.3072g3HbwK1BH.004096'
snap=pynbody.load(file)
snap.physical_units()
snap.families()
halos=snap.halos()
#using iord to find which halo the black hole is in
def findBH(snap):
    iord=snap.stars['iord']
    BHfilter = np.where(iord==101863510)
    BH = snap.stars[BHfilter]
    return BH
def findBHhalos(snap):
    BH = findBH(snap)
    BHhalos = BH['amiga.grp']
    return BHhalos
BHhalos = findBHhalos(snap)
print(BHhalos)