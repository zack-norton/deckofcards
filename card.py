import suite
import value

class Card():
	
	#init method
	def __init__(self, suite, value):
		self.suite = suite
		self.value = value

	def show(self):
		print(self.value.name + " of " + self.suite.name)