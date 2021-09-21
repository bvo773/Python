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

'''
41 - List
DOC: https://docs.python.org/3/tutorial/datastructures.html
A list is data structure.
 Data Structures: are methods or ways to organize and store data efficiently
 A variable can only store a single piece of data (int, string)
 A data structure can store grouped pieces of data (data that has relation or connection to each other)
 Eg) Store all the names of the US States together as one

Python List - A set of square brackets [] with many items stored inside. The items can be any data type.
It can even have a mixed data types [store strings, numbers, or set of booleans]
			index				0 		 1      2
 Eg) fruits = | [item1, item2, item3] 
					(begin)
 		 - item1 is at the beginning of the list (offset or a shift of 0)
		 - item2 is shifted from the beginning by 1 
		 - item3 is shifted from the beginning by 2
'''
def pythonList():
	usStates = ["California", "Illinois","Delaware","New York","Connecticut"]
	print(f'First element in list: {usStates[0]}') # first item
	print(f'Last element in the list: {usStates[-1]}') # last item in the last
	print(f'Second to last element in the list {usStates[-2]}')

	# Modify list to set a new piece of data
	usStates[0] = "Oregon" # At index 0, oregon is the new data 
	# Add an item to the end of the list: append()
	usStates.append("Binhlalaland")
	# Add multiple items to the list: extend(), extend the list by combining to the prev. list
	usStates.extend(["Yogurtland", "SnorlaxLand"])
	print(usStates)
	
pythonList()