import plotly.plotly as py
from math import exp
import pywt

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import distutils.dir_util




file1 = "New/config_withoutCharging_15.txt"
file2 = "New/config_withCharging_15.txt"


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
Gravity_chargingX  = []
Gravity_chargingY  = []
Gravity_chargingZ  = []

Z_Gravity_withoutCharging = []
Z_Magnetic_withoutCharging = []
Z_Gravity_withCharging    = []
Z_Magnetic_withCharging    = []

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
				Magnetic_timestamp_withoutCharging .append(int(w[1]))
			if w[0] == "Value:":
				Magnetic_withoutChargingX.append(float(w[1]))
				Magnetic_withoutChargingY.append(float(w[2]))
				Magnetic_withoutChargingZ.append(float(w[3]))
				Z_Magnetic_withoutCharging.append(15)

		elif flag == 1:
			if w[0] == "Time:":
				Gravity_timestamp_withoutCharging .append(int(w[1]))
			if w[0] == "Value:":
				Gravity_withoutChargingX.append(float(w[1]))
				Gravity_withoutChargingY.append(float(w[2]))
				Gravity_withoutChargingZ.append(float(w[3]))
				Z_Gravity_withoutCharging.append(15)



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
				Z_Magnetic_withCharging.append(15)

		elif flag == 1:
			if w[0] == "Time:":
				Gravity_timestamp_Charging .append(float(w[1]))
			if w[0] == "Value:":
				Gravity_chargingX.append(float(w[1]))
				Gravity_chargingY.append(float(w[2]))
				Gravity_chargingZ.append(float(w[3]))
				Z_Gravity_withCharging.append(15)


Magnetic_timestamp_Charging_15            = [ int((x - Magnetic_timestamp_Charging [0])/100000) for x in Magnetic_timestamp_Charging ]
Magnetic_timestamp_withoutCharging_15     = [ x - Magnetic_timestamp_withoutCharging [0] for x in Magnetic_timestamp_withoutCharging ]

Gravity_timestamp_Charging_15             = [ x - Gravity_timestamp_Charging [0] for x in Gravity_timestamp_Charging ]
Gravity_timestamp_withoutCharging_15      = [ x - Gravity_timestamp_withoutCharging [0] for x in Gravity_timestamp_withoutCharging ]


Magnetic_withoutChargingX_15 = Magnetic_withoutChargingX
Magnetic_withoutChargingY_15 = Magnetic_withoutChargingY
Magnetic_withoutChargingZ_15 = Magnetic_withoutChargingZ
Gravity_withoutChargingX_15  = Gravity_withoutChargingX
Gravity_withoutChargingY_15  = Gravity_withoutChargingY
Gravity_withoutChargingZ_15  = Gravity_withoutChargingZ

Magnetic_chargingX_15 = Magnetic_chargingX
Magnetic_chargingY_15 = Magnetic_chargingY
Magnetic_chargingZ_15 = Magnetic_chargingZ
Gravity_chargingX_15  = Gravity_chargingX
Gravity_chargingY_15  = Gravity_chargingY
Gravity_chargingZ_15  = Gravity_chargingZ


file1 = "New/config_withoutCharging_30.txt"
file2 = "New/config_withCharging_30.txt"


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
Gravity_chargingX  = []
Gravity_chargingY  = []
Gravity_chargingZ  = []

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
				Magnetic_timestamp_withoutCharging .append(int(w[1]))
			if w[0] == "Value:":
				Magnetic_withoutChargingX.append(float(w[1]))
				Magnetic_withoutChargingY.append(float(w[2]))
				Magnetic_withoutChargingZ.append(float(w[3]))
				Z_Magnetic_withoutCharging.append(30)

		elif flag == 1:
			if w[0] == "Time:":
				Gravity_timestamp_withoutCharging .append(int(w[1]))
			if w[0] == "Value:":
				Gravity_withoutChargingX.append(float(w[1]))
				Gravity_withoutChargingY.append(float(w[2]))
				Gravity_withoutChargingZ.append(float(w[3]))
				Z_Gravity_withoutCharging.append(30)



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
				Z_Magnetic_withCharging.append(30)

		elif flag == 1:
			if w[0] == "Time:":
				Gravity_timestamp_Charging .append(float(w[1]))
			if w[0] == "Value:":
				Gravity_chargingX.append(float(w[1]))
				Gravity_chargingY.append(float(w[2]))
				Gravity_chargingZ.append(float(w[3]))
				Z_Gravity_withCharging.append(30)


Magnetic_timestamp_Charging_30            = [ int((x - Magnetic_timestamp_Charging [0])/100000) for x in Magnetic_timestamp_Charging ]
Magnetic_timestamp_withoutCharging_30     = [ x - Magnetic_timestamp_withoutCharging [0] for x in Magnetic_timestamp_withoutCharging ]

Gravity_timestamp_Charging_30             = [ x - Gravity_timestamp_Charging [0] for x in Gravity_timestamp_Charging ]
Gravity_timestamp_withoutCharging_30      = [ x - Gravity_timestamp_withoutCharging [0] for x in Gravity_timestamp_withoutCharging ]


Magnetic_withoutChargingX_30 = Magnetic_withoutChargingX
Magnetic_withoutChargingY_30 = Magnetic_withoutChargingY
Magnetic_withoutChargingZ_30 = Magnetic_withoutChargingZ
Gravity_withoutChargingX_30  = Gravity_withoutChargingX
Gravity_withoutChargingY_30  = Gravity_withoutChargingY
Gravity_withoutChargingZ_30  = Gravity_withoutChargingZ

Magnetic_chargingX_30 = Magnetic_chargingX
Magnetic_chargingY_30 = Magnetic_chargingY
Magnetic_chargingZ_30 = Magnetic_chargingZ
Gravity_chargingX_30  = Gravity_chargingX
Gravity_chargingY_30  = Gravity_chargingY
Gravity_chargingZ_30  = Gravity_chargingZ

file1 = "New/config_withoutCharging_45.txt"
file2 = "New/config_withCharging_45.txt"


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
Gravity_chargingX  = []
Gravity_chargingY  = []
Gravity_chargingZ  = []

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
				Magnetic_timestamp_withoutCharging .append(int(w[1]))
			if w[0] == "Value:":
				Magnetic_withoutChargingX.append(float(w[1]))
				Magnetic_withoutChargingY.append(float(w[2]))
				Magnetic_withoutChargingZ.append(float(w[3]))
				Z_Magnetic_withoutCharging.append(45)

		elif flag == 1:
			if w[0] == "Time:":
				Gravity_timestamp_withoutCharging .append(int(w[1]))
			if w[0] == "Value:":
				Gravity_withoutChargingX.append(float(w[1]))
				Gravity_withoutChargingY.append(float(w[2]))
				Gravity_withoutChargingZ.append(float(w[3]))
				Z_Gravity_withoutCharging.append(45)



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
				Z_Magnetic_withCharging.append(45)

		elif flag == 1:
			if w[0] == "Time:":
				Gravity_timestamp_Charging .append(float(w[1]))
			if w[0] == "Value:":
				Gravity_chargingX.append(float(w[1]))
				Gravity_chargingY.append(float(w[2]))
				Gravity_chargingZ.append(float(w[3]))
				Z_Gravity_withCharging.append(45)


Magnetic_timestamp_Charging_45            = [ int((x - Magnetic_timestamp_Charging [0])/100000) for x in Magnetic_timestamp_Charging ]
Magnetic_timestamp_withoutCharging_45     = [ x - Magnetic_timestamp_withoutCharging [0] for x in Magnetic_timestamp_withoutCharging ]

Gravity_timestamp_Charging_45             = [ x - Gravity_timestamp_Charging [0] for x in Gravity_timestamp_Charging ]
Gravity_timestamp_withoutCharging_45      = [ x - Gravity_timestamp_withoutCharging [0] for x in Gravity_timestamp_withoutCharging ]


Magnetic_timestamp_Charging = Magnetic_timestamp_Charging_15 + Magnetic_timestamp_Charging_30 + Magnetic_timestamp_Charging_45
Magnetic_timestamp_withoutCharging = Magnetic_timestamp_withoutCharging_15 + Magnetic_timestamp_withoutCharging_30 + Magnetic_timestamp_withoutCharging_45
Gravity_timestamp_Charging = Gravity_timestamp_Charging_15 + Gravity_timestamp_Charging_30 + Gravity_timestamp_Charging_45
Gravity_timestamp_withoutCharging = Gravity_timestamp_withoutCharging_15 + Gravity_timestamp_withoutCharging_30 + Gravity_timestamp_withoutCharging_45

Magnetic_withoutChargingX_45 = Magnetic_withoutChargingX
Magnetic_withoutChargingY_45 = Magnetic_withoutChargingY
Magnetic_withoutChargingZ_45 = Magnetic_withoutChargingZ
Gravity_withoutChargingX_45  = Gravity_withoutChargingX
Gravity_withoutChargingY_45  = Gravity_withoutChargingY
Gravity_withoutChargingZ_45  = Gravity_withoutChargingZ

Magnetic_chargingX_45 = Magnetic_chargingX
Magnetic_chargingY_45 = Magnetic_chargingY
Magnetic_chargingZ_45 = Magnetic_chargingZ
Gravity_chargingX_45  = Gravity_chargingX
Gravity_chargingY_45  = Gravity_chargingY
Gravity_chargingZ_45  = Gravity_chargingZ

Magnetic_withoutChargingX =   Magnetic_withoutChargingX_15 + Magnetic_withoutChargingX_30 +Magnetic_withoutChargingX_45
Magnetic_withoutChargingY = Magnetic_withoutChargingY_15 + Magnetic_withoutChargingY_30 + Magnetic_withoutChargingY_45
Magnetic_withoutChargingZ = Magnetic_withoutChargingZ_15 + Magnetic_withoutChargingZ_30 + Magnetic_withoutChargingZ_45
Gravity_withoutChargingX  = Gravity_withoutChargingX_15 + Gravity_withoutChargingX_30 + Gravity_withoutChargingX_45
Gravity_withoutChargingY  = Gravity_withoutChargingY_15 + Gravity_withoutChargingY_30 + Gravity_withoutChargingY_45
Gravity_withoutChargingZ  = Gravity_withoutChargingZ_15 + Gravity_withoutChargingZ_30 + Gravity_withoutChargingZ_45

Magnetic_chargingX = Magnetic_chargingX_15 + Magnetic_chargingX_30 + Magnetic_chargingX_45
Magnetic_chargingY = Magnetic_chargingY_15 + Magnetic_chargingY_30 + Magnetic_chargingY_45
Magnetic_chargingZ = Magnetic_chargingZ_15 + Magnetic_chargingZ_30 + Magnetic_chargingZ_45
Gravity_chargingX  = Gravity_chargingX_15 + Gravity_chargingX_30 + Gravity_chargingX_45 
Gravity_chargingY  = Gravity_chargingY_15 + Gravity_chargingY_30 + Gravity_chargingY_45
Gravity_chargingZ  = Gravity_chargingZ_15 + Gravity_chargingZ_30 + Gravity_chargingZ_45



family = pywt.families()


for f in family:
	if(f=='bior' or f =='rbio'):
		f = f + '1.1'
	elif  f == 'coif' or f == 'db':
		f = f + '1'
	elif f == 'sym':
		f = f + '2'
	elif f == 'cgau' or f == 'gaus' or f =='mexh' or f == 'morl' or f == 'shan' or f == 'fbsp' or f == 'cmor' :
		continue

	myDwt15, mxDwt15 = pywt.dwt(Magnetic_chargingX_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Magnetic_chargingX_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Magnetic_chargingX_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_c = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_c = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_c = zDwt15 + zDwt30 + zDwt45


	myDwt15, mxDwt15 = pywt.dwt(Magnetic_withoutChargingX_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Magnetic_withoutChargingX_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Magnetic_withoutChargingX_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_wc = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_wc = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_wc = zDwt15 + zDwt30 + zDwt45

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(x_c, y_c , z_c ,c= 'blue' , zdir = 'z', marker = 'o')
	ax.scatter(x_wc, y_wc, z_wc,c= 'red' , zdir = 'z', marker = '^')
	ax.set_xlabel(f)
	ax.set_ylabel('Magnetic X')
	ax.set_zlabel('Distance')
	distutils.dir_util.mkpath('DwtF3D/' + f)
	plt.legend(loc='lower right')

	plt.savefig(('DwtF3D/' + f + "/MagneticX" ))



	myDwt15, mxDwt15 = pywt.dwt(Magnetic_chargingY_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Magnetic_chargingY_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Magnetic_chargingY_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_c = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_c = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_c = zDwt15 + zDwt30 + zDwt45


	myDwt15, mxDwt15 = pywt.dwt(Magnetic_withoutChargingY_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Magnetic_withoutChargingY_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Magnetic_withoutChargingY_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_wc = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_wc = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_wc = zDwt15 + zDwt30 + zDwt45

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(x_c, y_c , z_c ,c= 'blue' , zdir = 'z', marker = 'o')
	ax.scatter(x_wc, y_wc, z_wc,c= 'red' , zdir = 'z', marker = '^')
	ax.set_xlabel(f)
	ax.set_ylabel('Magnetic Y')
	ax.set_zlabel('Distance')
	distutils.dir_util.mkpath('DwtF3D/' + f)
	plt.savefig(('DwtF3D/' + f + "/MagneticY" ))


	myDwt15, mxDwt15 = pywt.dwt(Magnetic_chargingZ_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Magnetic_chargingZ_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Magnetic_chargingZ_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_c = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_c = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_c = zDwt15 + zDwt30 + zDwt45


	myDwt15, mxDwt15 = pywt.dwt(Magnetic_withoutChargingZ_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Magnetic_withoutChargingZ_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Magnetic_withoutChargingZ_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_wc = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_wc = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_wc = zDwt15 + zDwt30 + zDwt45

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(x_c, y_c , z_c ,c= 'blue' , zdir = 'z', marker = 'o')
	ax.scatter(x_wc, y_wc, z_wc,c= 'red' , zdir = 'z', marker = '^')
	ax.set_xlabel(f)
	ax.set_ylabel('Magnetic Z')
	ax.set_zlabel('Distance')
	distutils.dir_util.mkpath('DwtF3D/' + f)
	plt.savefig(('DwtF3D/' + f + "/MagneticZ" ))


	myDwt15, mxDwt15 = pywt.dwt(Gravity_chargingX_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Gravity_chargingX_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Gravity_chargingX_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_c = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_c = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_c = zDwt15 + zDwt30 + zDwt45


	myDwt15, mxDwt15 = pywt.dwt(Gravity_withoutChargingX_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Gravity_withoutChargingX_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Gravity_withoutChargingX_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_wc = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_wc = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_wc = zDwt15 + zDwt30 + zDwt45

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(x_c, y_c , z_c ,c= 'blue' , zdir = 'z', marker = 'o')
	ax.scatter(x_wc, y_wc, z_wc,c= 'red' , zdir = 'z', marker = '^')
	ax.set_xlabel(f)
	ax.set_ylabel('Gravity X')
	ax.set_zlabel('Distance')
	distutils.dir_util.mkpath('DwtF3D/' + f)
	plt.savefig(('DwtF3D/' + f + "/GravityX" ))


	myDwt15, mxDwt15 = pywt.dwt(Gravity_chargingY_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Gravity_chargingY_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Gravity_chargingY_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_c = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_c = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_c = zDwt15 + zDwt30 + zDwt45


	myDwt15, mxDwt15 = pywt.dwt(Gravity_withoutChargingY_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Gravity_withoutChargingY_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Gravity_withoutChargingY_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_wc = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_wc = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_wc = zDwt15 + zDwt30 + zDwt45

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(x_c, y_c , z_c ,c= 'blue' , zdir = 'z', marker = 'o')
	ax.scatter(x_wc, y_wc, z_wc,c= 'red' , zdir = 'z', marker = '^')
	ax.set_xlabel(f)
	ax.set_ylabel('Gravity Y')
	ax.set_zlabel('Distance')
	distutils.dir_util.mkpath('DwtF3D/' + f)
	plt.savefig(('DwtF3D/' + f + "/GravityY" ))


	myDwt15, mxDwt15 = pywt.dwt(Gravity_chargingZ_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Gravity_chargingZ_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Gravity_chargingZ_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_c = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_c = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_c = zDwt15 + zDwt30 + zDwt45


	myDwt15, mxDwt15 = pywt.dwt(Gravity_withoutChargingZ_15,f)
	zDwt15 = [15] * len(myDwt15)
	myDwt30, mxDwt30 = pywt.dwt(Gravity_withoutChargingZ_30,f)
	zDwt30 = [30] * len(myDwt30)

	myDwt45, mxDwt45 = pywt.dwt(Gravity_withoutChargingZ_45,f)
	zDwt45 = [45] * len(myDwt45)

	y_wc = myDwt15.tolist() + myDwt30.tolist() + myDwt45.tolist()
	x_wc = mxDwt15.tolist() + mxDwt30.tolist() + mxDwt45.tolist()
	z_wc = zDwt15 + zDwt30 + zDwt45

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(x_c, y_c , z_c ,c= 'blue' , zdir = 'z', marker = 'o')
	ax.scatter(x_wc, y_wc, z_wc,c= 'red' , zdir = 'z', marker = '^')
	ax.set_xlabel(f)
	ax.set_ylabel('Gravity Z')
	ax.set_zlabel('Distance')
	distutils.dir_util.mkpath('DwtF3D/' + f)
	plt.savefig(('DwtF3D/' + f + "/GravityZ" ))





'''
w,z = pywt.dwt(Magnetic_chargingX, 'db1')
x,y = pywt.dwt(Magnetic_withoutChargingX,'db1')
plt.plot(x,y, 'r', label = 'Without charging'  )
plt.plot(w,z, 'b', label = 'While charging')
plt.ylabel('Magnetic Field X axis')
plt.legend(loc='lower right')
plt.show()


w,z = pywt.dwt(Magnetic_chargingY, 'db1')
x,y = pywt.dwt(Magnetic_withoutChargingY,'db1')
plt.plot(x,y, 'r', label = 'Without charging'  )
plt.plot(w,z, 'b', label = 'While charging')
plt.ylabel('Magnetic Field Y axis')
plt.legend(loc='lower right')
plt.show()


w,z = pywt.dwt(Magnetic_chargingZ, 'db1')
x,y = pywt.dwt(Magnetic_withoutChargingZ,'db1')
plt.plot(x,y, 'r', label = 'Without charging'  )
plt.plot(w,z, 'b', label = 'While charging')
plt.ylabel('Magnetic Field Z axis')
plt.legend(loc='lower right')
plt.show()



w,z = pywt.dwt(Gravity_chargingX, 'db1')
x,y = pywt.dwt(Gravity_withoutChargingX,'db1')
plt.plot(x,y, 'r', label = 'Without charging'  )
plt.plot(w,z, 'b', label = 'While charging')
plt.ylabel('Gravity X axis')
plt.legend(loc='lower right')
plt.show()

w,z = pywt.dwt(Gravity_chargingY, 'db1')
x,y = pywt.dwt(Gravity_withoutChargingY,'db1')
plt.plot(x,y, 'r', label = 'Without charging'  )
plt.plot(w,z, 'b', label = 'While charging')
plt.ylabel('Gravity Y axis')
plt.legend(loc='lower right')
plt.show()

w,z = pywt.dwt(Gravity_chargingZ, 'db1')
x,y = pywt.dwt(Gravity_withoutChargingZ,'db1')
plt.plot(x,y, 'r', label = 'Without charging'  )
plt.plot(w,z, 'b', label = 'While charging')
plt.ylabel('Gravity Z axis')
plt.legend(loc='lower right')
plt.show()
'''


'''
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




temp = 0
Gravity_chargingX = [   x - (sum(Gravity_chargingX)/len(Gravity_chargingX)) for x in Gravity_chargingX ]
for i in Gravity_chargingX:
	temp += exp(-i)
Gravity_chargingX = [   exp(-x)/temp for x in Gravity_chargingX ]


temp = 0
Gravity_withoutChargingX = [   x - (sum(Gravity_withoutChargingX)/len(Gravity_withoutChargingX)) for x in Gravity_withoutChargingX ]
for i in Gravity_withoutChargingX:
	temp += exp(-i)
Gravity_withoutChargingX = [   exp(-x)/temp for x in Gravity_withoutChargingX ]


temp = 0
Gravity_chargingY = [   x - (sum(Gravity_chargingY)/len(Gravity_chargingY)) for x in Gravity_chargingY ]
for i in Gravity_chargingY:
	temp += exp(-i)
Gravity_chargingY = [   exp(-x)/temp for x in Gravity_chargingY ]


temp = 0
Gravity_withoutChargingY = [   x - (sum(Gravity_withoutChargingY)/len(Gravity_withoutChargingY)) for x in Gravity_withoutChargingY ]
for i in Gravity_withoutChargingY:
	temp += exp(-i)
Gravity_withoutChargingY = [   exp(-x)/temp for x in Gravity_withoutChargingY ]

temp = 0
Gravity_chargingZ = [   x - (sum(Gravity_chargingZ)/len(Gravity_chargingZ)) for x in Gravity_chargingZ ]
for i in Gravity_chargingZ:
	temp += exp(-i)
Gravity_chargingZ = [   exp(-x)/temp for x in Gravity_chargingZ ]


temp = 0
Gravity_withoutChargingZ = [   x - (sum(Gravity_withoutChargingZ)/len(Gravity_withoutChargingZ)) for x in Gravity_withoutChargingZ ]
for i in Gravity_withoutChargingZ:
	temp += exp(-i)
Gravity_withoutChargingZ = [   exp(-x)/temp for x in Gravity_withoutChargingZ ]
'''
'''
print 'tmp=',len(Magnetic_timestamp_Charging),Magnetic_timestamp_Charging[0] ,Magnetic_timestamp_Charging[len(Magnetic_timestamp_Charging)-1]
t = []
m = []
for x,y in zip(Magnetic_timestamp_Charging,Magnetic_chargingX):
	if len(t) > 0:
		i = x - t[len(t)-1]
	else:
		i = 0  
	while i>1:
		t.append(t[len(t)-1] + 1)
		m.append(m[len(m)-1])
		i-=1
		print 'i=',i
	t.append(x)
	m.append(y)


Magnetic_chargingX = m

#FFT
l1 = np.asarray(Magnetic_chargingY, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'b')

l1 = np.asarray(Magnetic_withoutChargingY, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'r')

plt.ylabel('Magnetic Field y axis')
plt.xlabel('Frequency')


plt.show()
'''
#FFT
'''
l1 = np.asarray(Magnetic_chargingX, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'b')

l1 = np.asarray(Magnetic_withoutChargingX, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'r')

plt.ylabel('Magnetic Field X axis')
plt.xlabel('Frequency')


plt.show()
#FFT
l1 = np.asarray(Magnetic_chargingZ, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'b')

l1 = np.asarray(Magnetic_withoutChargingZ, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'r')

plt.ylabel('Magnetic Field z axis')
plt.xlabel('Frequency')


plt.show()

#FFT
l1 = np.asarray(Gravity_chargingZ, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'b')

l1 = np.asarray(Gravity_withoutChargingZ, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'r')

plt.ylabel('Gravity z axis')
plt.xlabel('Frequency')


plt.show()



#FFT
l1 = np.asarray(Gravity_chargingY, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'b')

l1 = np.asarray(Gravity_withoutChargingY, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'r')

plt.ylabel('Gravity y axis')
plt.xlabel('Frequency')


plt.show()


#FFT
l1 = np.asarray(Gravity_chargingX, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'b')

l1 = np.asarray(Gravity_withoutChargingX, dtype=np.float)
fft_sequence = np.nan_to_num(np.fft.fft(l1))
fft_abs_sequence = np.absolute(fft_sequence)
freq = np.fft.fftfreq(len(l1))
plt.plot(freq,fft_abs_sequence,'r')

plt.ylabel('Gravity x axis')
plt.xlabel('Frequency')


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


plt.plot(Gravity_timestamp_withoutCharging,Gravity_withoutChargingX, 'r', label = 'Without charging'  )
plt.plot(Gravity_timestamp_Charging,Gravity_chargingX, 'b', label = 'While charging')
plt.ylabel('Gravity X axis')

#plt.plot(Gravity_timestamp_withoutCharging,Gravity_withoutChargingY, 'r', label = 'Without charging'  )
#plt.plot(Gravity_timestamp_Charging,Gravity_chargingY, 'b', label = 'While charging')
#plt.ylabel('Gravity Y axis')

#plt.plot(Gravity_timestamp_withoutCharging,Gravity_withoutChargingZ, 'r', label = 'Without charging'  )
#plt.plot(Gravity_timestamp_Charging,Gravity_chargingZ, 'b', label = 'While charging')
#plt.ylabel('Gravity Z axis')
'''
'''
plt.xlabel('Timestamp')
plt.legend(loc='lower right')

plt.show()
'''