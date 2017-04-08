from girls import Girl

class NormalGirl(Girl):
	'girl class for normal girls'

	def __init__(self, name, atr, mbudget, intelli, type):
		'constructor'
		Girl.__init__(self, name, atr, mbudget, intelli, type)
		self.status = 'single'
		self.bfname = ''
		self.happiness = 0