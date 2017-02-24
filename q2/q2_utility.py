from random import randint
from random import choice
import csv

def utility():

	BT = ['Miser', 'Geek', 'Generous']
	GT = ['Choosy', 'Normal', 'Desperate']
	GFT = ['Essential', 'Luxury', 'Utility']

	B = [('B'+str(i+1), randint(3,25), randint(36,120), randint(1,12), randint(2,16), choice(BT)) for i in range(10)]
	G = [('G'+str(i+1), randint(3,16), randint(5,20), randint(3,7), choice(GT)) for i in range(5)]
	GF = [('GFT'+str(i+1), randint(2, 110), randint(5,25), choice(GFT)) for i in range(50)]

	create('boys.csv', B)
	create('girls.csv', G)
	create('gifts.csv', GF)

def create(file, list):
	f = open(file, 'wr')
	writer = csv.writer(f, delimiter = ',')

	for i in list:
		writer.writerow(i)

	