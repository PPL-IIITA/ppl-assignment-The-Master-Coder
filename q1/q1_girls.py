class Girl:
	'Girl class for all girls'

	def __init__(self, name, atr, mbudget, intelli):
		self.name = name
		self.atr = atr
		self.mbudget = mbudget
		self.intelli = intelli
		self.status = 'single'
		self.bfname = ''

	def is_elligible(self, gfbudget):
		if (self.mbudget <= gfbudget):
			return True
		else:
			return False