class Couple:
	'couple class for all couples'

	def __init__(self, boy, girl):
		'constructor'
		self.boy = boy
		self.girl = girl
		self.happiness = 0
		self.compatibility = 0
		self.GFT = []

	def set_happiness(self):
		'set the happiness of a couple'
		self.happiness = self.boy.happiness + self.girl.happiness

	def set_compatibility(self):
		'set the compatibility of a couple'
		a = self.boy.gfbudget - self.girl.mbudget
		b = abs(self.boy.atr - self.girl.atr)
		c = abs(self.boy.intelli - self.girl.intelli)
		self.compatility = a+b+c