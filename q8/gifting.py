import logging
from math import exp, log10

class Gifting:
	'gifting mechanism'

	def gifting(self, C, GFT, choice):
		'gifting methods'
		logging.warning('Gifting session ahead:\n')
		for c in C:
			if (c.boy.type == 'Miser'):
				self.hp_miser(GFT, c, choice)

			if (c.boy.type == 'Generous'):
				self.hp_generous(GFT, c, choice)

			if (c.boy.type == 'Geek'):
				self.hp_geek(GFT, c, choice)

	def hp_miser(self, GFT, c, choice):
		'provides gifting logic for Miser type Boys and sets the Happiness of the commited Boy and Girl and the whole couple, also sets the Compatibility of the couple'
		v1 = 0
		v2 = 0
		for g in GFT:
			if (g.price == c.girl.mbudget) or (g.price-c.girl.mbudget <= 100) and (c.boy.gfbudget >= 0) and (c.boy.gfbudget - g.price > 0):
				if (g.type == 'Luxury'):
					v2 = v2 + 2*g.price
				else:
					v2 = v2 + g.price
				v1 = v1 + g.price
				c.GFT = c.GFT + [g]
				c.boy.gfbudget = c.boy.gfbudget - g.price
				logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + g.name + ' of price = ' + str(g.price) + ' rupees')

		self.gifting_choice(GFT, c, v1, v2, choice, 'Miser')

	def hp_generous(self, GFT, c, choice):
		'provides gifting logic for Generous type Boys and sets the Happiness of the commited Boy and Girl and the whole couple, also sets the Compatibility of the couple'
		v1 = 0
		v2 = 0
		for g in GFT:
			if ((g.price == c.boy.gfbudget) or (c.boy.gfbudget-g.price <= 300)) and (c.boy.gfbudget >= 0) and (c.boy.gfbudget - g.price > 0):
				if (g.type == 'Luxury'):
					v2 = v2 + 2*g.price
				else:
					v2 = v2 + g.price
				v1 = v1 + g.price
				c.GFT = c.GFT + [g]
				c.boy.gfbudget = c.boy.gfbudget - g.price
				logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + g.name + ' of price = ' + str(g.price) + ' rupees')
		
		self.gifting_choice(GFT, c, v1, v2, choice, 'Generous')
		
	def hp_geek(self, GFT, c, choice):
		'provides gifting logic for Geek type Boys and sets the Happiness of the commited Boy and Girl and the whole couple, also sets the Compatibility of the couple'
		v1 = 0
		v2 = 0
		for g in GFT:
			if (g.price == c.girl.mbudget) or (g.price-c.girl.mbudget <= 100) and (c.boy.gfbudget >= 0) and (c.boy.gfbudget - g.price > 0):
				if (g.type == 'Luxury'):
					v2 = v2 + 2*g.price
				else:
					v2 = v2 + g.price
				v1 = v1 + g.price
				c.GFT = c.GFT + [g]
				c.boy.gfbudget = c.boy.gfbudget - g.price
				logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + g.name + ' of price = ' + str(g.price) + ' rupees')

		for i in GFT:
			if (i not in c.GFT) and (i.type == 'luxury') and (i.price <= c.boy.gfbudget):
				v2 = v2 + 2*i.price
				v1 = v1 + i.price
				c.GFT = c.GFT + [i]
				c.boy.gfbudget = c.boy.gfbudget - i.price
				logging.info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + i.name + ' of price = ' + str(i.price) + ' rupees')
				break

		self.gifting_choice(GFT, c, v1, v2, choice, 'Geek')

	def gifting_choice(self, GFT, c, v1, v2, choice, btype):
		'do gifting according to choice'
		if (choice == 2):
			x = 0
			y = 0
			z = 0
			for g in c.GFT:
				if (g.type == 'Essential'):
					x = x + 1
				elif (g.type == 'Luxury'):
					y = y + 1
				else:
					z = z + 1
			if (x == 0):
				for g in GFT:
					if (g.type == 'Essential'):
						v2 = v2 + g.price
						v1 = v1 + g.price
						c.GFT = c.GFT + [g]
						break
			if (y == 0):
				for g in GFT:
					if (g.type == 'Luxury'):
						v2 = v2 + 2*g.price
						v1 = v1 + g.price
						c.GFT = c.GFT + [g]
						break

			if (z == 0):
				for g in GFT:
					if (g.type == 'Utility'):
						v2 = v2 + g.price
						v1 = v1 + g.price
						c.GFT = c.GFT + [g]
						break

		if (c.girl.type == 'Choosy'):
			c.girl.happiness = log10(v2)
		elif (c.girl.type == 'Normal'):
			c.girl.happiness = v1
		else:
			c.girl.happiness = exp(v1)

		if (btype == 'Miser'):
			c.boy.happiness = c.boy.gfbudget
		elif (btype == 'Geek'):
			c.boy.happiness = c.girl.intelli
		else:
			c.boy.happiness = c.girl.happiness
			
		c.set_happiness()
		c.set_compatibility()