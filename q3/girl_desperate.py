from girls import Girl

class DesperateGirl(Girl):
	'girl class for desperate girls'

	def __init__(self, name, atr, mbudget, intelli, type):
		'constructor'
		Girl.__init__(self, name, atr, mbudget, intelli, type)
		self.status = 'single'
		'''@ivar: relationship status of desperate girl'''
		self.bfname = ''
		'''@ivar: boyfriend name of desperate girl'''
		self.happiness = 0
		'''@ivar: happiness of desperate girl'''