#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nrLetters= int(input("How many letters would you like in your password?\n")) 
nrSymbols = int(input(f"How many symbols would you like?\n"))
nrNumbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# get a string of random letters for letters,symbols, and numbers
randomLetters = ""
randomSymbols = ""
randomNumbers = ""

for i in range(0,nrLetters): # not using i cause u are using a random index
  randomLetter = letters[random.randint(0,len(letters)-1)]
  randomLetters += str(randomLetter)

for i in range(0, nrSymbols):
  randomSymbol = symbols[random.randint(0,len(symbols)-1)]
  randomSymbols += str(randomSymbol)

for i in range(0, nrNumbers):
  randomNumber = numbers[random.randint(0, len(numbers)-1)]
  randomNumbers += str(randomNumber)

easyPassword = str(randomLetters + randomSymbols + randomNumbers)

print(f"Easy Password:\n {easyPassword}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# shuffle the characters in the string -> convert it into a list and use the random shuffle method and use the 
# join() method to concat the new shuffled list to an empty string
passwordList = list(easyPassword)
random.shuffle(passwordList)
hardPassword = "".join(passwordList)
print(f"Hard Password:\n {hardPassword}")
