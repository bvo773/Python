'''
DAY 4 - RANDOMISATION AND PYTHON LISTS
MODULE: random
DOC: https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
VID: https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
Methods:
- random.randint(a,b) // random int between a and b (both inclusive)
USE CASES:  
A DICE GAME, RANDOM  NAME GENERATOR, PASSWORD GENERATOR
A DRAWING RANDOMIZATION

NOTES
- To create a degree of unpredictability
- Computers are deterministic: They will perform repeatable actions in fully predictable ways
- Computer use Pseudorandomness
- a lock with 4 digit code: __  __ __ __
- It would take 26^4 combination to unlock it
- In theory, the person can unlock it if they wait long enough to unlock it by trying all 26^4 combinations
- So not 'TRUE RANDOMNESS'. PRACTICALLY SECURE NOT PERFECTLY SECURE
'''		

'''
39 - RANDOM MODULE
Module example car - different modules (engine, wheel, axles, etc)
module helps divide the code into different functionalities
'''
def importingModule():
	import my_module
	print(my_module.pi) # importing my module and acess the pi variable


def randomModule():
	import random
	randomInteger = random.randint(1,5) # [0,2] inclusive
	print(randomInteger)

	randomFloat = random.random()  #returns x within interval [0,1) 0.00000 - 0.99999
	print(randomFloat)

	#random decimal between 0 and 5 using random(): 0.000... - 4.9999..
	decimal = randomFloat * 5
	print ("Decimal: {:.2f}".format(decimal))

# instead of matching their names to TRUE or LOVE lettters
def loveScore():
	import random
	print(f"Your love score is {random.randint(1,100)}")

'''
40 - RANDOM EXERCISE
A virtual coin toss program. It will randomly tell the user "Heads" or "Tails"
'''
def coinToss():
	import random
	print("\"Heads\" or \"Tails\"?")
	
	enter = input("Hit \"ENTER\" to continue")
	if (enter == ""):
		randomSide = random.randint(0,1)
		if randomSide == 1:
			print(" Heads")
		else:
			print(" Tails")

