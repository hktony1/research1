import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt 
file='h229.cosmo50PLK.3072gst5HbwK1BH.000096'
snap=pynbody.load(file)
snap.physical_units()
snap.families()
halos=snap.halos()
def findBH(snap):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = snap.stars[BHfilter]
    return BH
def findBHhalos(snap):
    BH = findBH(snap)
    BHhalos = BH['amiga.grp']
    return BHhalos
BHhalos = findBHhalos(snap)