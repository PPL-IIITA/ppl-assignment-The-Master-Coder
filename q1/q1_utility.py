from random import randint
import csv

def utility():
	B = [('B'+str(i+1), randint(3,25), randint(36,120), randint(1,12), randint(2,16)) for i in range(10)]
	G = [('G'+str(i+1), randint(3,16), randint(5,20), randint(3,7)) for i in range(5)]

	create('boys.csv', B)
	create('girls.csv', G)

def create(file, list):
	f = open(file, 'wr')
	writer = csv.writer(f, delimiter = ',')

	for i in list:
		writer.writerow(i)