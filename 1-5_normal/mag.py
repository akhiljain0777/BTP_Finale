import distutils.dir_util
import matplotlib.pyplot as plt


def x(file1,file2):
	timestamp_WC = []
	magneticX_WC = []
	magneticY_WC = []
	magneticZ_WC = []
	Gravity_withoutChargingX = []
	Gravity_withoutChargingY = []
	Gravity_withoutChargingZ = []
	Gravity_timestamp_withoutCharging = []
	timestamp_C = []
	Gravity_timestamp_Charging = []
	magneticX_C = []
	magneticY_C = []
	magneticZ_C = []
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
					timestamp_WC.append(int(w[1]))
				if w[0] == "Value:":
					magneticX_WC.append(float(w[1]))
					magneticY_WC.append(float(w[2]))
					magneticZ_WC.append(float(w[3]))

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
					timestamp_C.append(float(w[1]))
				if w[0] == "Value:":
					magneticX_C.append(float(w[1]))
					magneticY_C.append(float(w[2]))
					magneticZ_C.append(float(w[3]))

			elif flag == 1:
				if w[0] == "Time:":
					Gravity_timestamp_Charging .append(float(w[1]))
				if w[0] == "Value:":
					Gravity_chargingX.append(float(w[1]))
					Gravity_chargingY.append(float(w[2]))
					Gravity_chargingZ.append(float(w[3]))

	timestamp_C           = [ x - timestamp_C [0] for x in timestamp_C ]
	timestamp_WC     = [ x - timestamp_WC [0] for x in timestamp_WC ]
	Gravity_timestamp_Charging            = [ x - Gravity_timestamp_Charging [0] for x in Gravity_timestamp_Charging ]
	Gravity_timestamp_withoutCharging      = [ x - Gravity_timestamp_withoutCharging [0] for x in Gravity_timestamp_withoutCharging ]

	distutils.dir_util.mkpath('Results/')
	print len(timestamp_C)
	print len(timestamp_WC)
	plt.plot(timestamp_WC,magneticX_WC, 'ro', label = 'Without charging'  )
	plt.plot(timestamp_C,magneticX_C, 'b^', label = 'While charging')
	plt.ylabel('Magnetic Field X axis')
	plt.xlabel('Timestamp')
	plt.legend(loc='lower right')
	plt.savefig("Results/MagneticX_15")
	plt.clf()

	plt.plot(timestamp_WC,magneticY_WC, 'ro', label = 'Without charging'  )
	plt.plot(timestamp_C,magneticY_C, 'b^', label = 'While charging')
	plt.ylabel('Magnetic Field Y axis')
	plt.xlabel('Timestamp')
	plt.legend(loc='lower right')
	plt.savefig("Results/MagneticY_15")
	plt.clf()


	plt.plot(timestamp_WC,magneticZ_WC, 'ro', label = 'Without charging'  )
	plt.plot(timestamp_C,magneticZ_C, 'b^', label = 'While charging')
	plt.ylabel('Magnetic Field Z axis')
	plt.xlabel('Timestamp')
	plt.legend(loc='lower right')
	plt.savefig("Results/MagneticZ_15")


	plt.plot(Gravity_timestamp_withoutCharging,Gravity_withoutChargingX, 'ro', label = 'Without charging'  )
	plt.plot(Gravity_timestamp_Charging,Gravity_chargingX, 'bo', label = 'While charging')
	plt.ylabel('Gravity Field X axis')
	plt.xlabel('Timestamp')
	plt.legend(loc='lower right')
	plt.savefig("Results/gravityX_15")
	plt.clf()

	plt.plot(Gravity_timestamp_withoutCharging,Gravity_withoutChargingY, 'ro', label = 'Without charging'  )
	plt.plot(Gravity_timestamp_Charging,Gravity_chargingY, 'bo', label = 'While charging')
	plt.ylabel('gravity Field Y axis')
	plt.xlabel('Timestamp')
	plt.legend(loc='lower right')
	plt.savefig("Results/gravityY_15")
	plt.clf()


	plt.plot(Gravity_timestamp_withoutCharging,Gravity_withoutChargingZ, 'ro', label = 'Without charging'  )
	plt.plot(Gravity_timestamp_Charging,Gravity_chargingZ, 'bo', label = 'While charging')
	plt.ylabel('gravity Field Z axis')
	plt.xlabel('Timestamp')
	plt.legend(loc='lower right')
	plt.savefig("Results/gravityZ_15")



file1 = "data/config_withoutCharging.txt"
file2 = "data/config_withCharging.txt"
x(file1,file2)

	
