'''
58 - FUNCTIONS|WHILE LOOPS|CODE BLOCKS
PROJECT: Have a robot complete any randomly generated maze
Built-in functions doc: https://docs.python.org/3/library/functions.html
'''

'''
59 - DEFINING AND CALLING PYTHON FUNCTIONS
FUNCTIONS allows us to group code of instructions and refer to them later by calling with one instruction
FunctionGame: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
FORMAT: def function_name() use def keyword, function name, then follows by a set of parentheses
Example-
  def functionName():
    #Do this
    #Then do this
    #Finally do this

Calling our functions:
  functionName()
'''
def myFunction():
  print("Hello")
  print("Binh!")

myFunction()

'''
60 - REEBORG HUDDLES CHALLENGE
FILE: hurdle_1.py

def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(6):
    jump()
'''

'''
61 - INDENTATION
DOC: https://www.python.org/dev/peps/pep-0008/
'''

'''
62 - WHILE LOOPS Important
FILE: hurdle_2.py
Note: can be stuck in INFINITE loop if condition is NEVER FALSE,
#usually use to evaluate if your (condition) is TRUE  until condition is FALSE loop stops

while something_is_true: 
  #Do something repeatedly 

for item in list_of_items:
  #Do something for each item

for number in range(a,b):  #create a range [a,b) and use the number within that range to do something
  print(number)
'''

'''
63 - HURDLES CHALLENGE USING WHILE LOOPS
FILE: hurdle_3.py
'''

'''
64 - HURDLES CHALLENGE JUMPING OVER HURDLES USING WHILE LOOPS
FILE: hurdle_4.py
'''

'''
65 - COMPLETE MAZE
FILE: maze_project.py
'''

'''
IF YOU ARE STRUGGLING, ITS OKAY, IT MEANS YOU ARE LEARNING. 
DONT interpret struggle as a bad thing, it means you are making PROGRESS! KEEP GOING!
'''