class Couple:
	'Couple class for all couples'

	def __init__(self, boy, girl):
		self.boy = boy
		self.girl = girl
		self.happiness = 0
		self.compatibility = 0
		self.GFT = []

	def set_happiness(self):
		self.happiness = self.boy.happiness + self.girl.happiness

	def set_compatibility(self):
		a = self.boy.gfbudget - self.girl.mbudget
		b = abs(self.boy.atr - self.girl.atr)
		c = abs(self.boy.intelli - self.girl.intelli)
		self.compatility = a+b+c