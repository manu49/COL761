import matplotlib.pyplot as plt
import time
import os
import sys

c = 0
f = 0
C = 0 #global
algo = sys.argv[2]

raw_input_file = sys.argv[1]
root = raw_input_file.replace('.txt','')

out_file = root + '_' + algo 
out_file = out_file + ".txt"
processed = open(out_file,'w')

#https://en.wikipedia.org/wiki/K-d_tree
file_obj = open(raw_input_file,'r')

lines = file_obj.readlines()

#https://en.wikipedia.org/wiki/K-d_tree
file_obj.close()

if(algo == "fsg"):
	c=0
	f=1
	
	for line in lines :
		
		if(line[0] == '#') :

			processed.write('t\n')
			
			c = 0
			f = 0
			f = f + 1
		
		elif((line.replace('\n','').isdigit()) == True) :

			c = 0
			temp = f
			f = 1 - temp
			

		elif(0 == f):

			c = c + 1
			new_line = 'v' + ' ' + str(c) + ' ' + line.replace('\n','') 
			f = 0

			new_line = new_line + '\n'

			f = 0
			processed.write(new_line)
		
		
		elif(1 == f):

			new_line = 'u' + ' ' + line.replace('\n','')

			new_line = new_line + '\n'
			f = 1

			processed.write(new_line)

else :
	vc = 0
	c = 0
	C = 0
	f = 1
	d_map = dict()
	
	
	for line in lines :
		
		if('#' == line[0]):

			temp = 't # ' + str(C)
			temp = temp + '\n'

			processed.write(temp)
			C = C+1

			c = 0
			#f = 0
			f = 1
			
		elif((line.replace('\n','').isdigit()) == True):

			temp = f

			c = 0
			c = 0
			f = f
			f = 1 - temp
			
		elif(0 == f):
			
			temp = line.replace('\n','')

			if(temp not in d_map) :

				f = 0
				d_map[temp] = vc

				#print(f)
				f = 0
				vc = vc+1
			
			new_line = 'v' + ' ' + str(c) + ' ' + str(d_map[temp])

			c = c+1
			new_line = new_line + '\n'
			c = c -1
			
			processed.write(new_line)
			c = c + 1
		
		
		elif(1 == f) :

			new_line = 'e' + ' ' + line.replace('\n','')
			f = 1
			new_line = new_line + '\n'

			c = c + 1
			processed.write(new_line)
			c = c -1
	

		
	
processed.close()