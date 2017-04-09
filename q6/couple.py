class Couple:
	'couple class for all couples'
	
	def __init__(self, boy, girl):
		'constructor'
		self.boy = boy
		'''@ivar: stores boy object of couple'''
		self.girl = girl
		'''@ivar: stores girl object of couple'''
		self.happiness = 0
		'''@ivar: happiness of couple'''
		self.compatibility = 0
		'''@ivar: compatibility of couple'''
		self.GFT = []
		'''@ivar: List to store all the gifts given, from boy to girl of a couple'''

	def set_happiness(self):
		'set the happiness of a couple'
		self.happiness = self.boy.happiness + self.girl.happiness

	def set_compatibility(self):
		'set the compatibility of a couple'
		a = self.boy.gfbudget - self.girl.mbudget
		b = abs(self.boy.atr - self.girl.atr)
		c = abs(self.boy.intelli - self.girl.intelli)
		self.compatibility = a+b+c