import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np
from math import exp
from nfft import nfft

file1 = "config_withoutCharging.txt"
file2 = "config_withCharging.txt"


flag = -1

Magnetic_timestamp_withoutCharging  = []
Gravity_timestamp_withoutCharging = []
Magnetic_withoutChargingX = []
Magnetic_withoutChargingY = []
Magnetic_withoutChargingZ = []
Gravity_withoutChargingX = []
Gravity_withoutChargingY = []
Gravity_withoutChargingZ = []

Magnetic_timestamp_Charging  = []
Gravity_timestamp_Charging = []
Magnetic_chargingX = []
Magnetic_chargingY = []
Magnetic_chargingZ = []
Gravity_chargingX = []
Gravity_chargingY = []
Gravity_chargingZ = []


with open(file1, "r") as f1:
	for x in f1:
		w = x.split(' ')
		if w[0] == "\n":
			continue
		if w[0] == "Sensor_Name:":
			if len(w) == 3:
				flag = 0
			elif len(w) == 2:
				flag = 1

		elif flag == 0:
			if w[0] == "Time:":
				Magnetic_timestamp_withoutCharging.append(int(w[1]))
			if w[0] == "Value:":
				Magnetic_withoutChargingX.append(float(w[1]))
				Magnetic_withoutChargingY.append(float(w[2]))
				Magnetic_withoutChargingZ.append(float(w[3]))

		elif flag == 1:
			if w[0] == "Time:":
				Gravity_timestamp_withoutCharging.append(int(w[1]))
			if w[0] == "Value:":
				Gravity_withoutChargingX.append(float(w[1]))
				Gravity_withoutChargingY.append(float(w[2]))
				Gravity_withoutChargingZ.append(float(w[3]))



with open(file2, "r") as f2:
	for x in f2:
		w = x.split(' ')
		if w[0] == "\n":
			continue
		if w[0] == "Sensor_Name:":
			if len(w) == 3 :
				flag = 0
			elif len(w) == 2:
				flag = 1

		elif flag == 0:
			if w[0] == "Time:":
				Magnetic_timestamp_Charging.append(float(w[1]))
			if w[0] == "Value:":
				Magnetic_chargingX.append(float(w[1]))
				Magnetic_chargingY.append(float(w[2]))
				Magnetic_chargingZ.append(float(w[3]))

		elif flag == 1:
			if w[0] == "Time:":
				Gravity_timestamp_Charging.append(float(w[1]))
			if w[0] == "Value:":
				Gravity_chargingX.append(float(w[1]))
				Gravity_chargingY.append(float(w[2]))
				Gravity_chargingZ.append(float(w[3]))



Magnetic_timestamp_Charging           = [ x - Magnetic_timestamp_Charging[0] for x in Magnetic_timestamp_Charging]
Magnetic_timestamp_withoutCharging    = [ x - Magnetic_timestamp_withoutCharging[0] for x in Magnetic_timestamp_withoutCharging]

Gravity_timestamp_Charging            = [ x - Gravity_timestamp_Charging[0] for x in Gravity_timestamp_Charging]
Gravity_timestamp_withoutCharging     = [ x - Gravity_timestamp_withoutCharging[0] for x in Gravity_timestamp_withoutCharging]



# Normalizing the readings using e^-value/sum(e^-values)
temp = 0
Magnetic_chargingX = [   x - (sum(Magnetic_chargingX)/len(Magnetic_chargingX)) for x in Magnetic_chargingX ]
for i in Magnetic_chargingX:
	temp += exp(-i)
Magnetic_chargingX = [   exp(-x)/temp for x in Magnetic_chargingX ]


temp = 0
Magnetic_withoutChargingX = [   x - (sum(Magnetic_withoutChargingX)/len(Magnetic_withoutChargingX)) for x in Magnetic_withoutChargingX ]
for i in Magnetic_withoutChargingX:
	temp += exp(-i)
Magnetic_withoutChargingX = [   exp(-x)/temp for x in Magnetic_withoutChargingX ]

temp = 0
Magnetic_chargingY = [   x - (sum(Magnetic_chargingY)/len(Magnetic_chargingY)) for x in Magnetic_chargingY ]
for i in Magnetic_chargingY:
	temp += exp(-i)
Magnetic_chargingY = [   exp(-x)/temp for x in Magnetic_chargingY ]


temp = 0
Magnetic_withoutChargingY = [   x - (sum(Magnetic_withoutChargingY)/len(Magnetic_withoutChargingY)) for x in Magnetic_withoutChargingY ]
for i in Magnetic_withoutChargingY:
	temp += exp(-i)
Magnetic_withoutChargingY = [   exp(-x)/temp for x in Magnetic_withoutChargingY ]


temp = 0
Magnetic_chargingZ = [   x - (sum(Magnetic_chargingZ)/len(Magnetic_chargingZ)) for x in Magnetic_chargingZ ]
for i in Magnetic_chargingZ:
	temp += exp(-i)
Magnetic_chargingZ = [   exp(-x)/temp for x in Magnetic_chargingZ ]


temp = 0
Magnetic_withoutChargingZ = [   x - (sum(Magnetic_withoutChargingZ)/len(Magnetic_withoutChargingZ)) for x in Magnetic_withoutChargingZ ]
for i in Magnetic_withoutChargingZ:
	temp += exp(-i)
Magnetic_withoutChargingZ = [   exp(-x)/temp for x in Magnetic_withoutChargingZ ]




#FFT
l1 = np.asarray(Magnetic_chargingY, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'b')

l1 = np.asarray(Magnetic_chargingY, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'r')

plt.show()




#plt.plot(Magnetic_timestamp_withoutCharging,Magnetic_withoutChargingZ, 'r', label = 'Without charging'  )
#plt.plot(Magnetic_timestamp_Charging,Magnetic_chargingZ, 'b', label = 'While charging')
#plt.ylabel('Magnetic Field Z axis')

#plt.plot(Magnetic_timestamp_withoutCharging,Magnetic_withoutChargingY, 'r', label = 'Without charging'  )
#plt.plot(Magnetic_timestamp_Charging,Magnetic_chargingY, 'b', label = 'While charging')
#plt.ylabel('Magnetic Field Y axis')

#plt.plot(Magnetic_timestamp_withoutCharging,Magnetic_withoutChargingX, 'r', label = 'Without charging'  )
#plt.plot(Magnetic_timestamp_Charging,Magnetic_chargingX, 'b', label = 'While charging')
#plt.ylabel('Magnetic Field X axis')


#plt.plot(Gravity_timestamp_withoutCharging,Gravity_withoutChargingX, 'r', label = 'Without charging'  )
#plt.plot(Gravity_timestamp_Charging,Gravity_chargingX, 'b', label = 'While charging')
#plt.ylabel('Gravity X axis')

#plt.plot(Gravity_timestamp_withoutCharging,Gravity_withoutChargingY, 'r', label = 'Without charging'  )
#plt.plot(Gravity_timestamp_Charging,Gravity_chargingY, 'b', label = 'While charging')
#plt.ylabel('Gravity Y axis')
'''
plt.plot(Gravity_timestamp_withoutCharging,Gravity_withoutChargingZ, 'r', label = 'Without charging'  )
plt.plot(Gravity_timestamp_Charging,Gravity_chargingZ, 'b', label = 'While charging')
plt.ylabel('Gravity Z axis')

plt.xlabel('Timestamp')
plt.legend(loc='lower right')

plt.show()
'''