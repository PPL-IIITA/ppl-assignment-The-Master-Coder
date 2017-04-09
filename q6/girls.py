class Girl:
	'girl class for all girls'

	def __init__(self, name, atr, mbudget, intelli, type):
		'constructor'
		self.name = name
		'''@ivar: name of girl'''
		self.atr = atr
		'''@ivar: attractiveness of girl'''
		self.mbudget = mbudget
		'''@ivar: maintainence budget of girl'''
		self.intelli = intelli
		'''@ivar: intelligence of girl'''
		self.type = type
		'''@ivar: type of girl'''

	def is_elligible(self, gfbudget):
		'checks the elligibility of a given Boy, for the current instance of Girl class'
		if (self.mbudget <= gfbudget):
			return True
		else:
			return False