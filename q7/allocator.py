from couple import Couple
import logging

class allocator:
	'allocates boyfriends to girls i.e. makes couples and stores them in different structures'

	def allocator1(self, B, G, GB, k):
		'allocates and stores in List'
		CP = []

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
		C = [Couple(c[0], c[1]) for c in CP]
		CB = []
		for c in C:
			CB.append(c.boy.name)

		for b in GB:
			if (b not in CB):
				print b + ' - ' + 'Error 404: No girlfriend found'
			else:
				for c in C:
					if (c.boy.name == b):
						print b + ' - ' + c.girl.name
						break


	def allocator2(self, B, G, GB, k):
		'allocates and stores in List(sorted)'
		CP = []

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
		C = [Couple(c[0], c[1]) for c in CP]
		C = sorted(C, key=lambda item: item.boy.name)
		CB = []
		for c in C:
			CB.append(c.boy.name)

		for b in GB:
			if (b not in CB):
				print b + ' - ' + 'Error 404: No girlfriend found'
			else:
				print b + ' - ' + self.binarySearch(C, b)
		


	def allocator3(self, B, G, GB, k):
		'allocates and stores in hash table'

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
		hash = {}
		for b in B:
			if (b.status == 'commited'):
				hash.update({b.name : b.gfname})
			else:
				hash.update({b.name : 'none'})

		for b in GB:
			if (hash[b] == 'none'):
				print b + ' - ' + 'Error 404: No girlfriend found'
			else:
				print b + ' - ' + hash[b]

	def binarySearch(self, alist, boyname):
		'carries out binary search on the Couples list for searching girlfriend of a given boy'
	    if len(alist) == 0:
	        return False
	    else:
	        midpoint = len(alist)//2
	        if alist[midpoint].boy.name == boyname:
	          return alist[midpoint].girl.name
	        else:
	          if boyname < alist[midpoint].boy.name:
	            return self.binarySearch(alist[:midpoint], boyname)
	          else:
	            return self.binarySearch(alist[midpoint+1:], boyname)