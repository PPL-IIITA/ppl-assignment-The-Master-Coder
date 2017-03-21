from q3_teens import Teen
class Girl(Teen):
	'girl class for all girls'

	def __init__(self, name, atr, mbudget, intelli, type):
		'constructor'
		Teen.__init__(self, name, atr, intelli, type)
		self.mbudget = mbudget
		self.bfname = ''

	def is_elligible(self, gfbudget):
		'checks the elligibility of a given Boy, for the current instance of Girl class'
		if (self.mbudget <= gfbudget):
			return True
		else:
			return False