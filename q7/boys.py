class Boy:
	'boy class for all boys'

	def __init__(self, name, atr, gfbudget, intelli, min_atr_req, type):
		'constructor'
		self.name = name
		self.atr = atr
		self.gfbudget = gfbudget
		self.intelli = intelli
		self.min_atr_req = min_atr_req
		self.type = type

	def is_elligible(self, mbudget, atr):
		'checks the elligibility of a given Girl, for the current instance of Boy class'
		if (self.gfbudget >= mbudget) and (atr >= self.min_atr_req):
			return True
		else:
			return False