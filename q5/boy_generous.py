from boys import Boy

class GenerousBoy(Boy):
	'boy class for generous boys'

	def __init__(self, name, atr, gfbudget, intelli, min_atr_req, type):
		'constructor'
		Boy.__init__(self, name, atr, gfbudget, intelli, min_atr_req, type)
		self.status = 'single'
		self.gfname = ''
		self.happiness = 0
