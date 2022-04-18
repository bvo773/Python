'''
File: main.py
Author: Binh Vo
'''
'''
############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer
'''


def dealCardsInitially(userCards, dealerCards, cards):
  for _ in range(2):
    userCards.append(random.choice(cards))
    dealerCards.append(random.choice(cards))

def showCurrentScores(userCards, dealerCards):
  print(f"\tYour cards: {userCards}, current score: {sum(userCards)}")
  print(f"\tComputer's first card: {dealerCards[0]}")

def getScore(deck):
  return sum(deck)

def dealAnotherCard(deck):
  card = random.choice(cards)
  if card == 11:
    if sum(deck) + 11 <= 21:
      deck.append(card)
    else:
      deck.append(1)
  else:
    deck.append(card)

def calculateFinalScores(userCards, dealerCards):
  userScore = sum(userCards)
  dealerScore = sum(dealerCards)
  print(f"\n\nYour final hand: {userCards}, final score: {userScore}")
  print(f"Computer's final hand: {dealerCards}, final score: {dealerScore}")

  if (userScore == dealerScore) or (userScore > 21 and dealerScore > 21):
    print("DRAW!")
  elif userScore == 21 and len(userCards) == 2:
    print("BLACKJACK, YOU WIN! 😊")
  elif dealerScore == 21 and len(dealerCards) == 2:
    print("BLACKJACK! CPU WIN! 😔")
  elif (userScore > dealerScore and userScore <= 21) or (dealerScore > 21 and userScore <= 21):
    print("YOU WIN! 😊")
  else:
    print("SORRY, YOU WENT OVER. YOU LOSE! 😔")
    
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
userCards = []
dealerCards = []

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play == 'y':
  play = True
else:
  play = False

while play:
  from art import logo
  print(logo)
  dealCardsInitially(userCards, dealerCards, cards)
  showCurrentScores(userCards, dealerCards)

  choice = input("\nType 'y' to get another card, type 'n' to pass: ").lower()

  dealerScore = getScore(dealerCards)

  while dealerScore < 17:
    dealAnotherCard(dealerCards)
    dealerScore = sum(dealerCards)

  while choice.lower() == 'y':
    dealAnotherCard(userCards)
    showCurrentScores(userCards,dealerCards)
    if sum(userCards) >= 21:
      break
    choice = input("\nType 'y' to get another card, type 'n' to pass: ").lower()

  calculateFinalScores(userCards, dealerCards)
  userCards = []
  dealerCards = []
  
  play = input("\nDo you want to continue playing Blackjack? Type 'y' or 'n': ").lower()
  if play.lower() == "y": play = True
  else: play = False



