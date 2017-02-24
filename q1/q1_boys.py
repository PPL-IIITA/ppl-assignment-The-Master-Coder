class Boy:
	'Boy class for all boys'

	def __init__(self, name, atr, gfbudget, intelli, min_atr_req):
		self.name = name
		self.atr = atr
		self.gfbudget = gfbudget
		self.intelli = intelli
		self.min_atr_req = min_atr_req
		self.status = 'single'
		self.gfname = ''

	def is_elligible(self, mbudget, atr):
		if (self.gfbudget >= mbudget) and (atr >= self.min_atr_req):
			return True
		else:
			return False