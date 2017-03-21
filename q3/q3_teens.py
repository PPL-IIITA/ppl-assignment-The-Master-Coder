import abc
class Teen:
	'teen class for boys and girls'
	__metaclass__ = abc.ABCMeta

	def __init__(self, name, atr, intelli, type):
		'constructor'
		self.name = name
		self.atr = atr
		self.intelli = intelli
		self.status = 'single'
		self.happiness = 0
		self.type = type

	@abc.abstractmethod
	def is_elligible(self):
		'abstract method which is overriden and overloaded by the Boy and Girl class respectively acc. to their needs'
		return