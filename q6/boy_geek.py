from boys import Boy

class GeekBoy(Boy):
	'boy class for geek boys'

	def __init__(self, name, atr, gfbudget, intelli, min_atr_req, type):
		'constructor'
		Boy.__init__(self, name, atr, gfbudget, intelli, min_atr_req, type)
		self.status = 'single'
		'''@ivar: relationship status of geek boy'''
		self.gfname = ''
		'''@ivar: girlfriend name of geek boy'''
		self.happiness = 0
		'''@ivar: happiness of geek boy'''
