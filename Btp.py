import matplotlib.pyplot as plt


file1 = "config_withoutCharging.txt"
file2 = "config_withCharging.txt"


flag = -1

ts_Gravitywith  = []
ts_Gravitywithout  = []
readings_GravitywithoutX = []
readings_GravitywithoutY = []
readings_GravitywithoutZ = []
readings_GravitywithX = []
readings_GravitywithY = []
readings_GravitywithZ = []


ts_Orientationwith  = []
ts_Orientationwithout  = []
readings_OrientationwithoutX = []
readings_OrientationwithoutY = []
readings_OrientationwithoutZ = []
readings_OrientationwithX = []
readings_OrientationwithY = []
readings_OrientationwithZ = []



ts_Gyroscopewith  = []
ts_Gyroscopewithout  = []
readings_GyroscopewithoutX = []
readings_GyroscopewithoutY = []
readings_GyroscopewithoutZ = []
readings_GyroscopewithX = []
readings_GyroscopewithY = []
readings_GyroscopewithZ = []


with open(file1, "r") as f1:
	for x in f1:
		w = x.split(' ')
		if w[0] == "\n":
			continue
		if w[0] == "Sensor_Name:":
			if "Gravity" in x :
				flag = 0
			elif "Orientation" in x:
				flag = 1
			elif "Gyroscope" in x:
				flag = 2

		elif flag == 0:
			if w[0] == "Time:":
				ts_Gravitywithout.append(int(w[1]))
			if w[0] == "Value:":
				readings_GravitywithoutX.append(float(w[1]))
				readings_GravitywithoutY.append(float(w[2]))
				readings_GravitywithoutZ.append(float(w[3]))

		elif flag == 1:
			if w[0] == "Time:":
				ts_Orientationwithout.append(int(w[1]))
			if w[0] == "Value:":
				readings_OrientationwithoutX.append(float(w[1]))
				readings_OrientationwithoutY.append(float(w[2]))
				readings_OrientationwithoutZ.append(float(w[3]))


		elif flag == 2:
			if w[0] == "Time:":
				ts_Gyroscopewithout.append(int(w[1]))
			if w[0] == "Value:":
				readings_GyroscopewithoutX.append(float(w[1]))
				readings_GyroscopewithoutY.append(float(w[2]))
				readings_GyroscopewithoutZ.append(float(w[3]))

cnt = 0
cnt1 = 0
flag = -1

with open(file2, "r") as f1:
	for x in f1:
		w = x.split(' ')
		if w[0] == "\n":
			continue
		if w[0] == "Sensor_Name:":
			if "Gravity" in x :
				flag = 0
			elif "Orientation" in x:
				flag = 1
			elif "Gyroscope" in x:
				flag = 2

		elif flag == 0:
			if w[0] == "Time:":
				ts_Gravitywith.append(int(w[1]))
			if w[0] == "Value:":
				readings_GravitywithX.append(float(w[1]))
				readings_GravitywithY.append(float(w[2]))
				readings_GravitywithZ.append(float(w[3]))

		elif flag == 1:
			if w[0] == "Time:":
				ts_Orientationwith.append(int(w[1]))
			if w[0] == "Value:":
				readings_OrientationwithX.append(float(w[1]))
				readings_OrientationwithY.append(float(w[2]))
				readings_OrientationwithZ.append(float(w[3]))


		elif flag == 2:
			if w[0] == "Time:":
				ts_Gyroscopewith.append(int(w[1]))
				cnt +=1
			if w[0] == "Value:":
				readings_GyroscopewithX.append(float(w[1]))
				readings_GyroscopewithY.append(float(w[2]))
				readings_GyroscopewithZ.append(float(w[3]))
				cnt1 +=1

print "bhai", len(readings_GyroscopewithZ)

ts_Gravitywith          = [ x - ts_Gravitywith[0] for x in ts_Gravitywith]
ts_Gravitywithout       = [ x - ts_Gravitywithout[0] for x in ts_Gravitywithout]
ts_Gyroscopewith        = [ x - ts_Gyroscopewith[0] for x in ts_Gyroscopewith]
ts_Gyroscopewithout     = [ x - ts_Gyroscopewithout[0] for x in ts_Gyroscopewithout]
ts_Orientationwith      = [ x - ts_Orientationwith[0] for x in ts_Orientationwith]
ts_Orientationwithout   = [ x - ts_Orientationwithout[0] for x in ts_Orientationwithout]


#plt.plot(ts_Gravitywithout,readings_GravitywithoutZ, 'r', label = 'Without charging'  )
#plt.plot(ts_Gravitywith,readings_GravitywithZ, 'b', label = 'While charging')
#plt.ylabel('Gravity Z axis')

#plt.plot(ts_Gravitywithout,readings_GravitywithoutY, 'r', label = 'Without charging'  )
#plt.plot(ts_Gravitywith,readings_GravitywithY, 'b', label = 'While charging')
#plt.ylabel('Gravity Y axis')


#plt.plot(ts_Gravitywithout,readings_GravitywithoutX, 'r', label = 'Without charging'  )
#plt.plot(ts_Gravitywith,readings_GravitywithX, 'b', label = 'While charging')
#plt.ylabel('Gravity X axis')

#plt.plot(ts_Orientationwithout,readings_OrientationwithoutX, 'r', label = 'Without charging'  )
#plt.plot(ts_Orientationwith,readings_OrientationwithX, 'b', label = 'While charging')
#plt.ylabel('Orientation X axis')

#plt.plot(ts_Orientationwithout,readings_OrientationwithoutY, 'r', label = 'Without charging'  )
#plt.plot(ts_Orientationwith,readings_OrientationwithY, 'b', label = 'While charging')
#plt.ylabel('Orientation Y axis')

#plt.plot(ts_Orientationwithout,readings_OrientationwithoutZ, 'r', label = 'Without charging'  )
#plt.plot(ts_Orientationwith,readings_OrientationwithZ, 'b', label = 'While charging')
#plt.ylabel('Orientation Z axis')

#plt.plot(ts_Gyroscopewithout,readings_GyroscopewithoutX, 'r', label = 'Without charging'  )
#plt.plot(ts_Gyroscopewith,readings_GyroscopewithX, 'b', label = 'While charging')
#plt.ylabel('Gyroscope X axis')


#plt.plot(ts_Gyroscopewithout,readings_GyroscopewithoutY, 'r', label = 'Without charging'  )
#plt.plot(ts_Gyroscopewith,readings_GyroscopewithY, 'b', label = 'While charging')
#plt.ylabel('Gyroscope Y axis')


plt.plot(ts_Gyroscopewithout,readings_GyroscopewithoutZ, 'r', label = 'Without charging'  )
plt.plot(ts_Gyroscopewith,readings_GyroscopewithZ, 'b', label = 'While charging')
plt.ylabel('Gyroscope Y axis')


plt.xlabel('Timestamp')
plt.legend(loc='lower right')

plt.show()