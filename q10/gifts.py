class Gift:
	'gift class for all gifts'

	def __init__(self, name, price, value, type):
		'constructor'
		self.name = name
		'''@ivar: name of the gift'''
		self.price = price
		'''@ivar: price of the gift'''
		self.value = value
		'''@ivar: value of the gift'''
		self.type = type
		'''@ivar: type of the gift'''
