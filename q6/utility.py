from random import randint
from random import choice
import csv

def utility():
	'creates the input csv files'
	BT = ['Miser', 'Geek', 'Generous']
	GT = ['Choosy', 'Normal', 'Desperate']
	GFT = ['Essential', 'Luxury', 'Utility']

	B = [('B'+str(i+1), randint(3,25), randint(36,120), randint(1,12), randint(2,16), choice(BT)) for i in range(10)]
	G = [('G'+str(i+1), randint(3,16), randint(5,20), randint(3,7), choice(GT)) for i in range(5)]
	GF = []

	for i in range(50):
		c = choice(GFT)
		if (c == 'Essential'):
			GF.append(['GFT'+str(i+1), randint(2, 110), randint(5,25), c])
		else:
			GF.append(['GFT'+str(i+1), randint(2, 110), randint(5,25), c, randint(1, 15), randint(1, 15)])

	create('boys.csv', B)
	create('girls.csv', G)
	create('gifts.csv', GF)

def create(file, list):
	'writes to csv files'
	f = open(file, 'wr')
	writer = csv.writer(f, delimiter = ',')

	for i in list:
		writer.writerow(i)

	