'''
DAY 4 - RANDOMISATION AND PYTHON LISTS
MODULE: random
DOC: https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
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
import random
 
random.seed(1) 
 
# Get the state of the generator
state = random.getstate()
 
print('Generating a random sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))

'''		
import random
