from q3_teens import Teen
class Boy(Teen):
	'boy class for all boys'

	def __init__(self, name, atr, gfbudget, intelli, min_atr_req, type):
		'constructor'
		Teen.__init__(self, name, atr, intelli, type)
		self.gfbudget = gfbudget
		self.min_atr_req = min_atr_req
		self.gfname = ''

	def is_elligible(self, mbudget, atr):
		'checks the elligibility of a given Girl, for the current instance of Boy class'
		if (self.gfbudget >= mbudget) and (atr >= self.min_atr_req):
			return True
		else:
			return False