from gifts import Gift

class EssentialGift(Gift):
	'gift class for essential gifts'

	def __init__(self, name, price, value, type):
		'constructor'
		Gift.__init__(self, name, price, value, type)