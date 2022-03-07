
'''
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

- Dealer - 10 Revealed
- You - Q Revealed

- Dealer deal another card 
  - dealer concealed
  - you can see your own card: 3

- Dealer deal another card
  - you can see your card: 7
  - Your total: 10 + 3 + 7 = 20

- If dealer score < 17, they must take another card

'''
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playBlackJack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
from art import logo
print(logo)

userCards = []
cpuCards = []

def dealCardsInitially():
  userCards.append(random.choice(cards))
  userCards.append(random.choice(cards))
  cpuCards.append(random.choice(cards))

dealCardsInitially()
print(f"\tYour cards: {userCards}, current score: {sum(userCards)}")
print(f"\tComputer's first card: {cpuCards[0]}")

def dealAnotherCard(userCards):
  userCards.append(random.choice(cards))

anotherCard = input("Type 'y' to get another card, type 'n' to pass").lower()
if totalCpuScore < 17:
      dealAnotherCard(cpuCards)
if anotherCard == 'y':
  dealAnotherCard(userCards)
  # if user score > 21, they automatically lose
else:
  # Calculate user and cpu scores and see who win
  totalCpuScore = sum(cpuCards)


