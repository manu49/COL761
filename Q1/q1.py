import matplotlib.pyplot as plt
import time
import os
import sys
out_file = sys.argv[2] 
out_file = "extra_ignore_.png"
input_file = sys.argv[1]

#print(m)
root = input_file.replace('.txt', '')


thresholds = [5.0,10.0,25.0,50.0,95.0]
#list = [95.0]

methods = ['gspan', 'fsg', 'gaston']
#methods = ['gaston']

dictionary = {}
for algo in methods :
	dictionary[algo] = []

exact_start = time.time()

start_time = time.time()
end_time = time.time()

for algo in methods :
	#print(algo)
	data = root + '_' + algo + '.txt'
	for s in thresholds:

		#print(str(s))

		if(algo == methods[0]):

			start_time = time.time()
			cmd = './Q1/gSpan6/gSpan -f ' + data + ' -s' +' ' + str(s/100.0) + ' ' +' -o' + ' >/dev/null 2>&1'
			
			#os.system(cmd)
			end_time = time.time()
			dictionary[algo].append(end_time-start_time)

		elif(algo == methods[1]):

			start_time = time.time()
			cmd = './Q1/pafi-1.0.1/Linux/fsg -s' + ' ' + str(s) + ' ' + data + ' >/dev/null 2>&1'
			
			os.system(cmd)
			end_time = time.time()
			dictionary[algo].append(end_time-start_time)

		elif(algo == methods[2]):

			start_time = time.time()
			cmd = './Q1/gaston-1.1-re/gaston' + ' ' + str((s*42682)/100.0) + ' ' + data + ' >/dev/null 2>&1'
			#cmd = '.
			
			os.system(cmd)
			end_time = time.time()
			dictionary[algo].append(end_time-start_time)

		else:

			break

		#print(end_time - start_time)

if(end_time - exact_start < 2000):
	time.sleep(2000-(end_time-exact_start))

vals1 = dictionary['gspan']
vals2 = dictionary['fsg']
vals3 = dictionary['gaston']

#print("done")

plt.plot(thresholds, vals1, label = "gspan")
plt.plot(thresholds, vals2, label = "fsg")
plt.plot(thresholds, vals3, label = "gaston")
plt.xlabel("Min Support Value")
plt.ylabel("Time (in seconds)")
plt.legend()
plt.savefig(out_file)



