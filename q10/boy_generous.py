from boys import Boy

class GenerousBoy(Boy):
	'boy class for generous boys'

	def __init__(self, name, atr, gfbudget, intelli, min_atr_req, type):
		'constructor'
		Boy.__init__(self, name, atr, gfbudget, intelli, min_atr_req, type)
		self.status = 'single'
		'''@ivar: relationship status of generous boy'''
		self.gfname = ''
		'''@ivar: girlfriend name of generous boy'''
		self.happiness = 0
		'''@ivar: happiness of generous boy'''
