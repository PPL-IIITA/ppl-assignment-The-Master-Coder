from girls import Girl

class ChoosyGirl(Girl):
	'girl class for choosy girls'

	def __init__(self, name, atr, mbudget, intelli, type):
		'constructor'
		Girl.__init__(self, name, atr, mbudget, intelli, type)
		self.status = 'single'
		'''@ivar: relationship status of choosy girl'''
		self.bfname = ''
		'''@ivar: boyfriend name of choosy girl'''
		self.happiness = 0
		'''@ivar: happiness of choosy girl'''