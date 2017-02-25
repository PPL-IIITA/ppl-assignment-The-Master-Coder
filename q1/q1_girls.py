class Girl:
	'girl class for all girls'

	def __init__(self, name, atr, mbudget, intelli):
		'constructor'
		self.name = name
		self.atr = atr
		self.mbudget = mbudget
		self.intelli = intelli
		self.status = 'single'
		self.bfname = ''

	def is_elligible(self, gfbudget):
		'checks the elligibility of a given Boy, for the current instance of Girl class'
		if (self.mbudget <= gfbudget):
			return True
		else:
			return False