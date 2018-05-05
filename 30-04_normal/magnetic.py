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


with open('zeroC.csv','r') as f:
	f = csv.reader(f, delimiter=',', quotechar='|')
	i = 0
	for x in f:
		i += 1
		if(i==1):
			continue
		if i==2000:
			break
		timestamp_C.append(x[0])
		magneticX_C.append(x[1])
		magneticY_C.append(x[2])
		magneticZ_C.append(x[3])

print("1", len(timestamp_C) )


with open('zeroWC.csv','r') as g:
	g = csv.reader(g, delimiter=',', quotechar='|')
	i = 0
	for x in g:
		i += 1
		if(i==1):
			continue
		if(i==2000):
			break
		timestamp_WC.append(x[0])
		magneticX_WC.append(x[1])
		magneticY_WC.append(x[2])
		magneticZ_WC.append(x[3])


print len(timestamp_WC)
print timestamp_C[len(timestamp_C) - 1]
print timestamp_WC[len(timestamp_WC) - 1]

#print timestamp_C
#print timestamp_WC

'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='2d')
ax.scatter(timestamp_WC,magneticX_WC, c= 'blue' ,  marker = 'o')
ax.scatter(x_wc, y_wc, z_wc,c= 'red' , marker = '^')
ax.set_xlabel(f)
ax.set_ylabel('Gravity Z')
ax.set_zlabel('Distance')


'''

plt.plot(timestamp_WC,magneticX_WC, 'r', label = 'Without charging'  )
plt.plot(timestamp_WC,magneticX_C, 'b', label = 'While charging')
plt.ylabel('Magnetic Field X axis')
plt.xlabel('Timestamp')
plt.legend(loc='lower right')
plt.savefig("Zero_MagneticX")
plt.clf()

plt.plot(timestamp_WC,magneticY_WC, 'ro', label = 'Without charging'  )
plt.plot(timestamp_C,magneticY_C, 'b^', label = 'While charging')
plt.ylabel('Magnetic Field Y axis')
plt.xlabel('Timestamp')
plt.legend(loc='lower right')
plt.savefig("Zero_MagneticY")
plt.clf()


plt.plot(timestamp_WC,magneticZ_WC, 'ro', label = 'Without charging'  )
plt.plot(timestamp_C,magneticZ_C, 'b^', label = 'While charging')
plt.ylabel('Magnetic Field Z axis')
plt.xlabel('Timestamp')
plt.legend(loc='lower right')
plt.savefig("Zero_MagneticZ")
