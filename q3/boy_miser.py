from boys import Boy

class MiserBoy(Boy):
	'boy class for miser boys'

	def __init__(self, name, atr, gfbudget, intelli, min_atr_req, type):
		'constructor'
		Boy.__init__(self, name, atr, gfbudget, intelli, min_atr_req, type)
		self.status = 'single'
		'''@ivar: relationship status of miser boy'''
		self.gfname = ''
		'''@ivar: girlfriend name of miser boy'''
		self.happiness = 0
		'''@ivar: happiness of miser boy'''
