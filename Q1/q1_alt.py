import time
import os
import numpy
from matplotlib import pyplot as plt
import sys

plotname = sys.argv[1] + ".png"
x_vals = [5.0,10.0,25.0,50.0,95.0]

gspan = [58, 49, 44, 30, 20]
gspan_secs = [3540, 1302, 368, 125, 10] #[(x*60) for x in gspan]


fsg = [59, 47, 39.6, 23.8, 18.2]
fsg_secs = [3540, 1515, 489, 203, 11] #[(x*60) for x in fsg]

gaston = [58, 46.7, 38.1, 20.7, 15.9]
gaston_secs = [300, 100, 56, 21, 9] #[(x*60) for x in gaston]

plt.plot(x_vals, gaston_secs, label = "gaston")
plt.plot(x_vals, fsg_secs, label = "fsg")
plt.plot(x_vals, gspan_secs, label = "gspan")
plt.xlabel("Min Support Value")
plt.ylabel("Time (in seconds)")
plt.legend()
plt.savefig(plotname)
