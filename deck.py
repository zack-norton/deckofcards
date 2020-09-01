import card
import random

class Deck():

	def __init__(self):
		self.cards = []

		for data in card.suite.Suite:
			for val in card.value.Value:
				self.cards.append(card.Card(data, val))

	def deal(self):
		return self.cards.pop()

	def shuffle(self):
		if(len(self.cards) == 52):
			random.shuffle(self.cards)
		else:
			print("Bad Deck")



if __name__ == '__main__':
	deck = Deck()
	deck.shuffle()
	card = deck.deal()
	card.show()