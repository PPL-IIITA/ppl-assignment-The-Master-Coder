from girls import Girl

class DesperateGirl(Girl):
	'girl class for desperate girls'

	def __init__(self, name, atr, mbudget, intelli, type):
		'constructor'
		Girl.__init__(self, name, atr, mbudget, intelli, type)
		self.status = 'single'
		self.bfname = ''
		self.happiness = 0