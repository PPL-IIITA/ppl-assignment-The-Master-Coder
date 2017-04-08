from boys import Boy
from girls import Girl
from couple import Couple
from gifts import Gift
from utility import utility
from gift_essential import EssentialGift
from gift_luxury import LuxuryGift
from gift_utility import UtilityGift
from girl_choosy import ChoosyGirl
from girl_normal import NormalGirl
from girl_desperate import DesperateGirl
from boy_miser import MiserBoy
from boy_generous import GenerousBoy
from boy_geek import GeekBoy
from gifting import Gifting

from random import randint
import csv
import logging

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p',
					level=logging.DEBUG,
                    filename='log.txt',
                    filemode='w')

def allocate():
	'reads and stores the input from the boys.csv and girls.csv files and then makes the valid couples'

	B = []
	G = []
	CP = []

	with open('boys.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for row in reader:
			if (row[5] == 'Miser'):
				B.append(MiserBoy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), row[5]))
			elif (row[5] == 'Generous'):
				B.append(GenerousBoy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), row[5]))
			else:
				B.append(GeekBoy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), row[5]))
		csvfile.close()

	with open('girls.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for row in reader:
			if (row[4] == 'Choosy'):
				G.append(ChoosyGirl(row[0], int(row[1]), int(row[2]), int(row[3]), row[4]))
			elif (row[4] == 'Normal'):
				G.append(NormalGirl(row[0], int(row[1]), int(row[2]), int(row[3]), row[4]))
			else:
				G.append(DesperateGirl(row[0], int(row[1]), int(row[2]), int(row[3]), row[4]))
		csvfile.close()

	logging.warning('Girls are checking out boys ahead:\n')
	for g in G:
		for b in B:
			logging.info('Commitment:  Girl: ' + g.name + '  is checking out  Boy: ' + b.name)
			if (b.is_elligible(g.mbudget, g.atr)) and (g.is_elligible(b.gfbudget)) and g.status == 'single' and b.status == 'single':
				g.status = 'commited'
				b.status = 'commited'
				g.bfname = b.name
				b.gfname = g.name
				logging.info('Commitment:  Girl: ' + g.name + '  got commited with  Boy: ' + b.name)
				CP = CP+[(b, g)]
				break

	print 'Couples formed:\n'
	for g in G:
		if g.status == 'single':
			print 'Girl: ' + g.name + '  is not commited to anyone'
		else:
			print 'Girl: ' + g.name + '  is commited with  Boy: ' + g.bfname

	print '\n'
	C = [Couple(c[0], c[1]) for c in CP]
	calculate_happiness(C)


def calculate_happiness(C):
	'reads and stores the inputs from the gifts.csv file and provide gift exchanges between the couples'
	GFT = []
	with open('gifts.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for row in reader:
			if (row[3] == 'Essential'):
				GFT.append(EssentialGift(row[0], int(row[1]), int(row[2]), row[3]))
			elif (row[5] == 'Luxury'):
				GFT.append(LuxuryGift(row[0], int(row[1]), int(row[2]), row[3], int(row[4]), int(row[5])))
			else:
				GFT.append(UtilityGift(row[0], int(row[1]), int(row[2]), row[3], int(row[4]), int(row[5])))
		csvfile.close()

	GFT = sorted(GFT, key=lambda item: item.price)

	print 'Choose your Gifting method:\n1 - Default Method\n2 - New method'
	while True:
		try:
			choice = int(raw_input())
			print '\n'
			a = Gifting()
			a.gifting(C, GFT, choice)
			print_gifts(C)
			break
		except:
			print 'Error: Input is not valid, please enter a valid input'

def print_gifts(C):
	'prints all the Gifts gifted by Boyfriend to his Girlfriend for all the Couples'
	for c in C:
		print 'Gifts given from Boy:  ' + c.boy.name + '  to Girl:  ' + c.girl.name + ':'
		for g in c.GFT:
			print 'Gift named:  ' + g.name + '  of type:  ' + g.type
		print '\n'
		k = randint(1, len(C))
	print_hc(C, k)


def print_hc(C, k):
	'prints the k most Happy Couples and k most Compatible Couples'
	A = sorted(C, key=lambda item: item.happiness, reverse=True)
	B = sorted(C, key=lambda item: item.compatibility, reverse=True)
	print str(k) + ' most Happy couples:'
	for i in range(k):
		print A[i].boy.name + ' and ' + A[i].girl.name

	print '\n' + str(k) + ' most Compatible couples:'
	for i in range(k):
		print B[i].boy.name + ' and ' + B[i].girl.name

utility()
allocate()