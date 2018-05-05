import csv 

data = []
with open('data_train.csv','r') as f:
	f = csv.reader(f, delimiter=',', quotechar='|')
	i = 0
	for x in f:
		data.append(x)


l = len(data)
i = 0
train = []
test = []
while float(i) < 0.9*float(len(data)): 
	train.append(data[i])
	i+=1

while float(i)< len(data):
	test.append(data[i])
	i+=1


with open('train.csv', 'wb') as csvfile:
	f = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for x in train:
		f.writerow(x)


with open('test.csv', 'wb') as csvfile:
	f = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for x in test:
		f.writerow(x)
