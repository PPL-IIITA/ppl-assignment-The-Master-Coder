from gifts import Gift

class LuxuryGift(Gift):
	'gift class for luxury gifts'

	def __init__(self, name, price, value, type, lxry_rtng, difficulty):
		'constructor'
		Gift.__init__(self, name, price, value, type)
		self.lxry_rtng = lxry_rtng
		'''@ivar: luxury rating of the luxury gift'''
		self.difficulty = difficulty
		'''@ivar: difficulty to obtain the luxury gift'''