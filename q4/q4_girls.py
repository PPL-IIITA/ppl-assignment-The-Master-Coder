class Girl:
	'girl class for all girls'

	def __init__(self, name, atr, mbudget, intelli, type):
		'constructor'
		self.name = name
		self.atr = atr
		self.mbudget = mbudget
		self.intelli = intelli
		self.status = 'single'
		self.bfname = ''
		self.happiness = 0
		self.type = type

	def is_elligible(self, gfbudget):
		'checks the elligibility of a given Boy, for the current instance of Girl class'
		if (self.mbudget <= gfbudget):
			return True
		else:
			return False