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
from allocator import allocator

import csv
import logging
import random
from random import randint

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p',
					level=logging.DEBUG,
                    filename='log.txt',
                    filemode='w')

def allocate():
	'reads and stores the input from the boys.csv and girls.csv files and then makes the valid couples'

	B = []
	G = []
	
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

	BN = []
	for b in B:
		BN.append(b.name)
	a = allocator()
	k = randint(1, len(BN))
	GB = random.sample(BN, k)
	print 'Given Boys list:'
	for b in GB:
		print b
	print '\n'

	print 'Choose your Allocator method:\n1 - List\n2 - List(sorted)\n3 - Hash table'

	choice = randint(1, 3)
	print choice
	print '\nGirlfriends for given boys:'
	if (choice == 2):
		a.allocator2(B, G, GB, k)
	elif (choice == 3):
		a.allocator3(B, G, GB, k)
	else:
		a.allocator1(B, G, GB, k)
	

utility()
allocate()