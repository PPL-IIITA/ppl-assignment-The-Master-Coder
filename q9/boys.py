class Boy:
	'boy class for all boys'

	def __init__(self, name, atr, gfbudget, intelli, min_atr_req, type):
		'constructor'
		self.name = name
		'''@ivar: name of boy'''
		self.atr = atr
		'''@ivar: attractiveness of boy'''
		self.gfbudget = gfbudget
		'''@ivar: girlfriend budget of boy'''
		self.intelli = intelli
		'''@ivar: intelligence of boy'''
		self.min_atr_req = min_atr_req
		'''@ivar: minimum attractiveness requirement of boy'''
		self.type = type
		'''@ivar: type of boy'''

	def is_elligible(self, mbudget):
		'checks the elligibility of a given Girl, for the current instance of Boy class'
		if (self.gfbudget >= mbudget):
			return True
		else:
			return False