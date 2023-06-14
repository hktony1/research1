import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt 
#this is how to load a snapshot using pynbody
file='/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000225/h229.cosmo50PLK.3072gst5HbwK1BH.000225'
snap=pynbody.load(file)
#turn weird simulated unitsinto units we use
snap.physical_units()
#this loads the halo data
halos=snap.halos()
#idx is just the halo id
idx=0
halo=halos[idx]
#this line finds the center position of the halo 
center=pynbody.analysis.halo.center(halo,mode='hyb',retcen=True)
print(center)