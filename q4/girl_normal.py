from girls import Girl

class NormalGirl(Girl):
	'girl class for normal girls'

	def __init__(self, name, atr, mbudget, intelli, type):
		'constructor'
		Girl.__init__(self, name, atr, mbudget, intelli, type)
		self.status = 'single'
		'''@ivar: relationship status of normal girl'''
		self.bfname = ''
		'''@ivar: boyfriend name of normal girl'''
		self.happiness = 0
		'''@ivar: happiness of normal girl'''