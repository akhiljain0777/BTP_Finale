import csv
import matplotlib.pyplot as plt
import plotly.plotly as py
import pywt



timestamp_C =  []
timestamp_WC = []
magneticX_C = []
magneticY_C = []
magneticZ_C = []
magneticx_WC = []
magneticy_WC = []
magneticZ_WC = []


with open('mag_C.csv','r') as f:
	f = csv.reader(f, delimiter=',', quotechar='|')
	i = 0
	for x in f:
		i += 1
		if(i==1):
			continue
		#if i==20000:
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
		#if(i==20000):
		#	break
		timestamp_WC.append(x[0])
		magneticx_WC.append(x[1])
		magneticy_WC.append(x[2])
		magneticZ_WC.append(x[3])


print len(timestamp_WC)
print timestamp_C[len(timestamp_C) - 1]
print timestamp_WC[len(timestamp_WC) - 1]

print timestamp_C
print timestamp_WC

y_C, x_C = pywt.dwt(magneticX_C,'db2')
y_WC, x_WC = pywt.dwt(magneticx_WC,'db2')

print len(y_C)

'''
plt.plot(x_WC,y_WC, 'ro', label = 'Without charging'  )
plt.plot(x_C,y_C, 'b^', label = 'While charging')
plt.ylabel('Magnetic Field X axis')
plt.xlabel('Frequency')
plt.legend(loc='lower right')
plt.savefig("MagneticX")
plt.clf()


y_C, x_C = pywt.dwt(magneticY_C,'db2')
y_WC, x_WC = pywt.dwt(magneticy_WC,'db2')

print len(y_C)

plt.plot(x_WC,y_WC, 'ro', label = 'Without charging'  )
plt.plot(x_C,y_C, 'b^', label = 'While charging')
plt.ylabel('Magnetic Field Y axis')
plt.xlabel('Frequency')
plt.legend(loc='lower right')
plt.savefig("MagneticY")
plt.clf()


y_C, x_C = pywt.dwt(magneticZ_C,'db2')
y_WC, x_WC = pywt.dwt(magneticZ_WC,'db2')


plt.plot(x_WC,y_WC, 'ro', label = 'Without charging'  )
plt.plot(x_C,y_C, 'b^', label = 'While charging')
plt.ylabel('Magnetic Field Z axis')
plt.xlabel('Frequency')
plt.legend(loc='lower right')
plt.savefig("MagneticZ")
plt.clf()
'''