'''
DAY 4 - RANDOMISATION AND PYTHON LISTS ***
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
41 - RANDOM MODULE (Pseudrandom number generators)
Module example car - different modules (engine, wheel, axles, etc)
module helps divide the code into different functionalities
'''
def importingModule():
	import my_module
	print(my_module.pi) # importing my module and acess the pi variable

# Importing random module
def randomModule():
	import random
	randomInteger = random.randint(1,5) # [0,2] inclusive
	print(randomInteger)

	randomFloat = random.random()  #returns x within interval [0,1) 0.00000 - 0.99999
	print(randomFloat)

  #to get float number multiply it with an intenger
  #random decimal between 0 and 5 using random(): 0.000... - 4.9999..
	randomFloat = randomFloat * randomInteger
	print ("Random Float: {:.2f}".format(randomFloat))

randomModule()

# instead of matching their names to TRUE or LOVE lettters
def loveScore():
	import random
	print(f"Your love score is {random.randint(1,100)}")

'''
42 - [Interacting Coding Exercise] RANDOM EXERCISE
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
43 - List
DOC: https://docs.python.org/3/tutorial/datastructures.html
A list is data structure. It has methods or ways to organize and store data efficiently
A variable can only store a single piece of data (int, string)
A data structure can store grouped pieces of data (data that has relation or connection to each other)
Eg) Store all the names of the US States together as one

Python List - A set of square brackets [] with many items stored inside. The items can be any data type.
It can even have a mixed data types [store strings, numbers, or set of booleans]
			index				   0 		    1        2
	Eg) fruits = | ["cherry", "apple", "pear"] 
						     (begin)
			- cherry is at the beginning of the list (offset or a shift of 0)
			- apple is 'shifted' from the beginning by 1 
			- pear is 'shifted' from the beginning by 2
'''
def pythonList():
	usStates = ["California", "Illinois","Delaware","New York","Connecticut"]
	print(f'First element in list: {usStates[0]}') # first item
	print(f'Last element in the list: {usStates[-1]}') # last item in the last
	print(f'Second to last element in the list {usStates[-2]}') # the  before the last item

	# Modify list to set a new piece of data
	usStates[0] = "Oregon" # At index 0, oregon is the new data 
	# Add an item to the end of the list: append()
	usStates.append("Binhlalaland")
	# Add multiple items to the list: extend(), extend the list by combining to the prev. list
	usStates.extend(["Yogurtland", "SnorlaxLand"])
	print(usStates)
	
'''
42 - Bankers Roulete Who Pays The Bill: at the end of the meal, rich bankers put all their credit cards in a bowl, whoever card is drawn pays the bill
Method: str.split(), random.randint(), random.choice()
Documentation:
- random.choice(): https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
- string to List: https://www.askpython.com/python/string/convert-string-to-list-in-python
'''
def bankerRoulete():
	import random
  # param: the character(s) to split -> ", " (comma and blank space) and return a list of strings without characters ', '
	rich_bankers = str(input("Participant bank players separated by a comma.\n ")).split(", ") 
	person_who_paid = random.choice(rich_bankers)
	# person_who_paid = rich_bankers[random.randint(0, len(rich_bankers)-1)]
	print(f"{person_who_paid} is going to pay the Bill!")

'''
44 - IndexErrors and working with nested lists
		0      1
[item1,item2][2]  -> IndexError: list index out of range

TIP:use len() to check the size of the list

Nested lists - list within a list
'''
def hightPesticidesFood():
	'''dirtyDozen = ["Strawberries", "Spinach", "Kale", "Nectaries", "Apples", "Grapes",
	"Peaches", "Cherries"]'''

	fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries",
	"Pears"]

	vegetables = ["Spinach","Kale","Tomatoe","Celery","Potatoes"]

	# create a nested list to combine the list for a list of dirty dozen
	dirtyDozen = [fruits, vegetables] # a list containing 2 lists
	print(dirtyDozen)
	print(dirtyDozen[0])
	print(dirtyDozen[1])
	# accessing a nested lists: r x c -> arr[row][column]
	print(dirtyDozen[0][1])
	print(dirtyDozen[1][2])
	print(dirtyDozen[1][3])

'''
46 - Treasure Map exercise: https://replit.com/@BinhVo2/day-4-3-exercise#README.md
Row 3, Column 2 would be entered as: 32
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']
'''

def treasureMap():
# 🚨 Don't change the code below 👇
	row1 = ["⬜️","⬜️","⬜️"]
	row2 = ["⬜️","⬜️","⬜️"]
	row3 = ["⬜️","⬜️","⬜️"]
	map = [row1, row2, row3]
	print(f"{row1}\n{row2}\n{row3}")
	position = input("Where do you want to put the treasure? (Row,Column) eg. 23: ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
	column = int(position[0]) - 1
	row = int(position[1]) - 1
	map[row][column] = "X"

#selected_row = map[row]
#selected_row[column] = "X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
	print(f"{row1}\n{row2}\n{row3}")

def treasureMapYu():
	# 🚨 Don't change the code below 👇
	row1 = ["⬜️","⬜️","⬜️"]
	row2 = ["⬜️","⬜️","⬜️"]
	row3 = ["⬜️","⬜️","⬜️"]
	map = [row1, row2, row3]
	print(f"{row1}\n{row2}\n{row3}")
	position = input("Where do you want to put the treasure? (Column,Row) eg. 23: ")

	column = int(position[0]) - 1
	row = int(position[1]) - 1

	# python understand multidimensioanl list by [row,col] 
	map[row][column] = "X"

	print(f"{map[0]}\n{map[1]}\n{map[2]}")
'''
47 - Rock Paper Scissors
'''
def rockPaperScissors():
  rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''

  paper = '''
      _______
  ---'   ____)____
            ______)
            _______)
          _______)
  ---.__________)
  '''

  scissors = '''
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  '''

  #Write your code below this line 👇
  import random
  resultList = [rock, paper, scissors]
  cpuChoice = random.randint(0,2)
  userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

  if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number, you lose!")
  else:
    print(resultList[userChoice])
    print(f"Computer chose: \n{resultList[cpuChoice]}")
    # user - rock, cpu paper
    if userChoice == 0 and cpuChoice == 1: 
      print("You lose!")
    elif userChoice == 0 and cpuChoice == 2:
      print("You win!")
    elif userChoice == 1 and cpuChoice == 0:
      print("You win!")
    elif userChoice == 1 and cpuChoice == 2:
      print("You lose!")
    elif userChoice == 2 and cpuChoice == 0:
      print("You lose!")
    elif userChoice == 2 and cpuChoice == 1:
      print("You win!")
    else:
      print("Draw!")

rockPaperScissors()
