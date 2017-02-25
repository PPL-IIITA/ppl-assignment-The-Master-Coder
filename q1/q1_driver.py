from q1_boys import Boy
from q1_girls import Girl
from q1_utility import utility
import csv
import logging

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p',
					level=logging.DEBUG,
                    filename='log.txt',
                    filemode='w')

def allocate():
	'reads and stores the inputs from the generated csv files and then makes the valid couples'

	with open('boys.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		B = [Boy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])) for row in reader]
		csvfile.close()

	with open('girls.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		G = [Girl(row[0], int(row[1]), int(row[2]), int(row[3])) for row in reader]
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
				break

	print 'Couples formed:\n'
	for g in G:
		if g.status == 'single':
			print 'Girl: ' + g.name + '  is not commited to anyone'
		else:
			print 'Girl: ' + g.name + '  is commited with  Boy: ' + g.bfname

utility()
allocate()	