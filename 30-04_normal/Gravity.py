import csv
import matplotlib.pyplot as plt

timestamp_C =  []
timestamp_WC = []
gravityX_C = []
gravityY_C = []
gravityZ_C = []
gravityX_WC = []
gravityY_WC = []
gravityZ_WC = []


with open('zeroC_grv.csv','r') as f:
	f = csv.reader(f, delimiter=',', quotechar='|')
	i = 0
	for x in f:
		i += 1
		if(i==1):
			continue
		#if i==2000:
		#	break
		timestamp_C.append(x[0])
		gravityX_C.append(x[1])
		gravityY_C.append(x[2])
		gravityZ_C.append(x[3])



with open('zeroWc_grv.csv','r') as f:
	f = csv.reader(f, delimiter=',', quotechar='|')
	i = 0
	for x in f:
		i += 1
		if(i==1):
			continue
		#if(i==2000):
		#	break
		timestamp_WC.append(x[0])
		gravityX_WC.append(x[1])
		gravityY_WC.append(x[2])
		gravityZ_WC.append(x[3])


print len(timestamp_WC)
'''
plt.plot(timestamp_WC,gravityX_WC, 'r', label = 'Without charging'  )
plt.plot(timestamp_C,gravityX_C, 'b', label = 'While charging')
plt.ylabel('Gravity Field X axis')
plt.xlabel('Timestamp')
plt.legend(loc='lower right')
plt.savefig("gravityX")
plt.clf()

plt.plot(timestamp_WC,gravityY_WC, 'ro', label = 'Without charging'  )
plt.plot(timestamp_C,gravityY_C, 'bo', label = 'While charging')
plt.ylabel('gravity Field Y axis')
plt.xlabel('Timestamp')
plt.legend(loc='lower right')
plt.savefig("gravityY")
plt.clf()


plt.plot(timestamp_WC,gravityZ_WC, 'ro', label = 'Without charging'  )
plt.plot(timestamp_C,gravityZ_C, 'bo', label = 'While charging')
plt.ylabel('gravity Field Z axis')
plt.xlabel('Timestamp')
plt.legend(loc='lower right')
plt.savefig("gravityZ")
'''