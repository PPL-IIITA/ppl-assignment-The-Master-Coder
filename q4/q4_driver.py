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
from random import randint
import csv
import logging
from math import exp, log10

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
	calculate_happiness(B, G, C)

def calculate_happiness(B, G, C):
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
	logging.warning('Gifting session ahead:\n')
	for c in C:
		if (c.boy.type == 'Miser'):
			hp_miser(GFT, c)

		if (c.boy.type == 'Generous'):
			hp_generous(GFT, c)

		if (c.boy.type == 'Geek'):
			hp_geek(GFT, c)

	k = randint(1, len(C))
	print_sc(C, k)
	newallocate(B, G, C, k)

def set_girl_happiness(c, v1, v2):
	'sets the happiness of a girl according to her type'
	if (c.girl.type == 'Choosy'):
		c.girl.happiness = log10(v2)
	elif (c.girl.type == 'Normal'):
		c.girl.happiness = v1
	else:
		c.girl.happiness = exp(v1)

def hp_miser(GFT, c):
	'provides gifting logic for Miser type Boys and sets the Happiness of the commited Boy and the whole couple, also sets the Compatibility of the couple'
	v1 = 0
	v2 = 0
	for g in GFT:
		if (g.price == c.girl.mbudget) or (g.price-c.girl.mbudget <= 100) and (c.boy.gfbudget_used >= 0) and (c.boy.gfbudget_used - g.price > 0):
			if (g.type == 'Luxury'):
				v2 = v2 + 2*g.price
			else:
				v2 = v2 + g.price
			v1 = v1 + g.price
			c.GFT = c.GFT + [g]
			c.boy.gfbudget_used = c.boy.gfbudget_used - g.price
			logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + g.name + ' of price = ' + str(g.price) + ' rupees')

	set_girl_happiness(c, v1, v2)
	c.boy.happiness = c.boy.gfbudget_used
	c.set_happiness()
	c.set_compatibility()

def hp_generous(GFT, c):
	'provides gifting logic for Generous type Boys and sets the Happiness of the commited Boy and the whole couple, also sets the Compatibility of the couple'
	v1 = 0
	v2 = 0
	for g in GFT:
		if ((g.price == c.boy.gfbudget_used) or (c.boy.gfbudget_used-g.price <= 300)) and (c.boy.gfbudget_used >= 0) and (c.boy.gfbudget_used - g.price > 0):
			if (g.type == 'Luxury'):
				v2 = v2 + 2*g.price
			else:
				v2 = v2 + g.price
			v1 = v1 + g.price
			c.GFT = c.GFT + [g]
			c.boy.gfbudget_used = c.boy.gfbudget_used - g.price
			logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + g.name + ' of price = ' + str(g.price) + ' rupees')
	set_girl_happiness(c, v1, v2)
	c.boy.happiness = c.girl.happiness
	c.set_happiness()
	c.set_compatibility()

def hp_geek(GFT, c):
	'provides gifting logic for Geek type Boys and sets the Happiness of the commited Boy and the whole couple, also sets the Compatibility of the couple'
	v1 = 0
	v2 = 0
	for g in GFT:
		if (g.price == c.girl.mbudget) or (g.price-c.girl.mbudget <= 100) and (c.boy.gfbudget_used >= 0) and (c.boy.gfbudget_used - g.price > 0):
			if (g.type == 'Luxury'):
				v2 = v2 + 2*g.price
			else:
				v2 = v2 + g.price
			v1 = v1 + g.price
			c.GFT = c.GFT + [g]
			c.boy.gfbudget_used = c.boy.gfbudget_used - g.price
			logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + g.name + ' of price = ' + str(g.price) + ' rupees')

	for i in GFT:
		if (i not in c.GFT) and (i.type == 'luxury') and (i.price <= c.boy.gfbudget_used):
			v2 = v2 + 2*i.price
			v1 = v1 + i.price
			c.GFT = c.GFT + [i]
			c.boy.gfbudget_used = c.boy.gfbudget_used - i.price
			logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + i.name + ' of price = ' + str(i.price) + ' rupees')
			break


	set_girl_happiness(c, v1, v2)
	c.boy.happiness = c.girl.intelli
	c.set_happiness()
	c.set_compatibility()

def print_sc(C, k):
	'prints the k least happy Couples'
	S = sorted(C, key=lambda item: item.happiness)
	print str(k) + ' least happy couples:'
	for i in range(k):
		print S[i].boy.name + ' and ' + S[i].girl.name


def newallocate(B, G, C, k):
	'allocates new boys to the girls who broke up'

	S = sorted(C, key=lambda item: item.happiness)
   	R = []

	for i in range(k):
		for c in C:
			if (S[i].girl.name == c.girl.name):
				c.boy.status = 'single'
				c.boy.gfname = ''
				c.boy.happiness = 0
				c.girl.status = 'single'
				c.girl.bfname = ''
				c.girl.happiness = 0
				R = R+[c]
				break

	for r in R:
		C.remove(r)

   	print '\nRemaining couples after Valentines Day(i.e. after breakups):\n'
	for g in G:
		if g.status == 'single':
			print 'Girl: ' + g.name + '  is not commited to anyone'
		else:
			print 'Girl: ' + g.name + '  is commited with  Boy: ' + g.bfname

	logging.warning('Heart-broken Girls are checking out new boys ahead:\n')
	for r in R:
		for b in B:
			logging.info('Commitment:  Girl: ' + r.girl.name + '  is checking out  Boy: ' + b.name)
			if (b.is_elligible(r.girl.mbudget, r.girl.atr)) and (r.girl.is_elligible(b.gfbudget)) and r.girl.status == 'single' and b.status == 'single' and b.name != r.boy.name:
				r.girl.status = 'commited'
				b.status = 'commited'
				r.girl.bfname = b.name
				b.gfname = r.girl.name
				logging.info('Commitment:  Girl: ' + r.girl.name + '  got commited with  Boy: ' + b.name)
				C = C + [(b,r.girl)]
				break

	print '\nNew Couples formed after breakups:\n'
	for g in G:
		if g.status == 'single':
			print 'Girl: ' + g.name + '  is not commited to anyone'
		else:
			print 'Girl: ' + g.name + '  is commited with  Boy: ' + g.bfname

utility()
allocate()
