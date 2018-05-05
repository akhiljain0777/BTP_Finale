import csv
import matplotlib.pyplot as plt
import plotly.plotly as py
from random import shuffle
import pywt




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
		timestamp_WC.append(x[0])
		magneticX_WC.append(x[1])
		magneticY_WC.append(x[2])
		magneticZ_WC.append(x[3])

print len(timestamp_C)
print len(timestamp_WC)

magneticX_C  = magneticX_C[0:min(len(timestamp_C),len(timestamp_WC))]
magneticY_C  = magneticY_C[0:min(len(timestamp_C),len(timestamp_WC))]
magneticZ_C  = magneticZ_C[0:min(len(timestamp_C),len(timestamp_WC))]
magneticX_WC = magneticX_C[0:min(len(timestamp_C),len(timestamp_WC))]
magneticY_WC = magneticY_C[0:min(len(timestamp_C),len(timestamp_WC))]
magneticZ_WC = magneticZ_C[0:min(len(timestamp_C),len(timestamp_WC))]

Gravity_withoutChargingX = []
Gravity_withoutChargingY = []
Gravity_withoutChargingZ = []
Gravity_timestamp_withoutCharging = []
Gravity_timestamp_Charging = []
Gravity_chargingX = []
Gravity_chargingY = []
Gravity_chargingZ = []

with open('gra_C.csv','r') as f:
	f = csv.reader(f, delimiter=',', quotechar='|')
	i = 0
	for x in f:
		i += 1
		if(i==1):
			continue
		#if i==200:
		#	break
		Gravity_timestamp_Charging.append(float(x[0]))
		Gravity_chargingX.append(x[1])
		Gravity_chargingY.append(x[2])
		Gravity_chargingZ.append(x[3])

print("1", len(timestamp_C) )


with open('gra_WC.csv','r') as f:
	f = csv.reader(f, delimiter=',', quotechar='|')
	i = 0
	for x in f:
		i += 1
		if(i==1):
			continue
		Gravity_timestamp_withoutCharging.append(float(x[0]))
		Gravity_withoutChargingX.append(x[1])
		Gravity_withoutChargingY.append(x[2])
		Gravity_withoutChargingZ.append(x[3])



'''
file1 = "config_withoutCharging.txt"
file2 = "config_withCharging.txt"


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
				continue
			if w[0] == "Value:":
				continue
		elif flag == 1:
			if w[0] == "Time:":
				Gravity_timestamp_withoutCharging .append(int(w[1]))
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
				continue
			if w[0] == "Value:":
				continue

		elif flag == 1:
			if w[0] == "Time:":
				Gravity_timestamp_Charging .append(float(w[1]))
			if w[0] == "Value:":
				Gravity_chargingX.append(float(w[1]))
				Gravity_chargingY.append(float(w[2]))
				Gravity_chargingZ.append(float(w[3]))
'''

Gravity_timestamp_Charging            = [ x - Gravity_timestamp_Charging [0] for x in Gravity_timestamp_Charging ]
Gravity_timestamp_withoutCharging      = [ x - Gravity_timestamp_withoutCharging [0] for x in Gravity_timestamp_withoutCharging ]

print len(Gravity_timestamp_Charging)
print len(Gravity_timestamp_withoutCharging)

Gravity_chargingX = Gravity_chargingX[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]
Gravity_chargingY = Gravity_chargingY[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]
Gravity_chargingZ = Gravity_chargingZ[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]
Gravity_withoutChargingX = Gravity_withoutChargingX[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]
Gravity_withoutChargingY = Gravity_withoutChargingY[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]
Gravity_withoutChargingZ = Gravity_withoutChargingZ[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]

magneticX_C  = magneticX_C[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]
magneticY_C  = magneticY_C[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]
magneticZ_C  = magneticZ_C[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]
magneticX_WC  = magneticX_WC[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]
magneticY_WC  = magneticY_WC[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]
magneticZ_WC  = magneticZ_WC[0:min(len(Gravity_timestamp_Charging),len(Gravity_timestamp_withoutCharging))]




mx_yC, mx_xC = pywt.dwt(magneticX_C,'db2')
mx_yWC, mx_xWC = pywt.dwt(magneticX_WC,'db2')


my_yC, my_xC = pywt.dwt(magneticY_C,'db2')
my_yWC, my_xWC = pywt.dwt(magneticY_WC,'db2')


mz_yC, mz_xC = pywt.dwt(magneticZ_C,'db2')
mz_yWC, mz_xWC = pywt.dwt(magneticZ_WC,'db2')


gx_yC, gx_xC = pywt.dwt(Gravity_chargingX,'db2')
gx_yWC, gx_xWC = pywt.dwt(Gravity_withoutChargingX,'db2')


gy_yC, gy_xC = pywt.dwt(Gravity_chargingY,'db2')
gy_yWC, gy_xWC = pywt.dwt(Gravity_withoutChargingY,'db2')


gz_yC, gz_xC = pywt.dwt(Gravity_chargingZ,'db2')
gz_yWC, gz_xWC = pywt.dwt(Gravity_withoutChargingZ,'db2')



finalData = []
for a,b,c,d,e,f,g,h,i,j,k,l in zip(mx_yC, mx_xC,my_yC, my_xC,mz_yC, mz_xC,gx_yC, gx_xC, gy_yC, gy_xC,gz_yC, gz_xC ):
	finalData.append([a,b,c,d,e,f,g,h,i,j,k,l,'Charging'])

for a,b,c,d,e,f,g,h,i,j,k,l in zip(mx_yWC, mx_xWC, my_yWC, my_xWC, mz_yWC, mz_xWC, gx_yWC, gx_xWC, gy_yWC, gy_xWC, gz_yWC, gz_xWC  ):
	finalData.append([a,b,c,d,e,f,g,h,i,j,k,l,'NotCharging'])

shuffle(finalData)


with open('data_train.csv', 'wb') as csvfile:
	f = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for x in finalData:
		f.writerow(x)
