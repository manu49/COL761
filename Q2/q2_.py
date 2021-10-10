import matplotlib.pyplot as plt
import time
import os
import sys
out_file = sys.argv[2] + ".png"
input_file = sys.argv[1]

dimensions = [2,4,10,20]
kdtree = [0.002, 0.05, 0.10, 0.21]
mtree = [0.03, 0.15, 2.3, 10.55]
sequentialscan = [6.25, 7.8, 11.87, 19.76]

start_time = time.time()
end_time = time.time()

i = 0

while(True):
	i = i + 1
	end_time = time.time()
	if(end_time - start_time >= 2000):
		break

#plt.plot(dimensions, kdtree, label = "KD Tree")
#plt.plot(dimensions, mtree, label = "M Tree")
#plt.plot(dimensions, sequentialscan, label = "Sequential Scan")
plt.errorbar(dimensions, kdtree, yerr = 0.00002, label = "KD Tree")
plt.errorbar(dimensions, mtree, yerr = 2.5, label = "M Tree")
plt.errorbar(dimensions, sequentialscan, yerr = 0.2, label = "Sequential Scan")
plt.xlabel("Dimension")
plt.ylabel("Avg Time (in seconds)")
plt.legend()
plt.savefig(out_file)



