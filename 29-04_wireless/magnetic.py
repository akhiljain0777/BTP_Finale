import csv
import matplotlib.pyplot as plt
import plotly.plotly as py


timestamp_C =  []
timestamp_WC = []
magneticX_C = []
magneticY_C = []
magneticZ_C = []
magneticX_WC = []
magneticY_WC = []
magneticZ_WC = []


with open('mag_C.csv','r') as f:
	f = csv.reader(f, delimiter=',', quotechar='|')
	i = 0
	for x in f:
		i += 1
		if(i==1):
			continue
		#if i==200:
		#	break
		timestamp_C.append(x[0])
		magneticX_C.append(x[1])
		magneticY_C.append(x[2])
		magneticZ_C.append(x[3])

print("1", len(timestamp_C) )


with open('mag_WC.csv','r') as f:
	f = csv.reader(f, delimiter=',', quotechar='|')
	i = 0
	for x in f:
		i += 1
		if(i==1):
			continue
		#if(i==200):
		#	break
		timestamp_WC.append(x[0])
		magneticX_WC.append(x[1])
		magneticY_WC.append(x[2])
		magneticZ_WC.append(x[3])


print len(timestamp_WC)
#print timestamp_C[len(timestamp_C) - 1]
#print timestamp_WC[len(timestamp_WC) - 1]

