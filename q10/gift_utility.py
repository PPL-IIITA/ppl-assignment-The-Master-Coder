from gifts import Gift

class UtilityGift(Gift):
	'gift class for utility gifts'

	def __init__(self, name, price, value, type, utlty_value, utlty_class):
		'constructor'
		Gift.__init__(self, name, price, value, type)
		self.utlty_value = utlty_value
		'''@ivar: utility value of the utility gift'''
		self.utlty_class = utlty_class
		'''@ivar: utility class of the utility gift'''