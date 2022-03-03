'''
DAY 8 FUNCTION PARAMETERS AND CAESAR CIPHER
Topics: Functions with Inputs, Arguments, Parameters
Project: Caesar Cpipher (encode and decode with a shift value)

Example)
SHIFT by 3
A B C D E
D E F G H
'''

'''
81 - FUNCTIONS
use 'def' keyword

def myFunction():
  # Do this
  # Then do this
  # Finally do this
myFuction()

# Functions with Inputs to do something with that data
# PARAMETER (name of the data that is being passed in and we refer to it inside the function) - something
# ARGUMENT (actual value of the data it is passed to the function) - 123
def myFunction(something):
  # Do this with 'something'
  # Then do this
  # Finally do this
myFuction(123)

'''
#Simple Function
def greet():
  print("Hello World")
  print("How are you? ")
  print("Isn't the weather nice today")

#Function that allows for input
def greetWithName(name):
  print(f"Hello {name}")
  print(f"How do you {name}? ")
  print(f"Isn't the weather nice today?")


'''
82 - Positional vs. Keyword Arguments
POSITIONAL Arguments (Default way calling functions) 
def myFunction(a, b, c):
  #Do this with a
  #Do this with b
  #Do this with c

myFunction(1,2,3) #Positional Arguments
myFunction(b = 2, a = 1, c = 3) #Keyword Arguments
'''
#Functions with more than 1 input
def greetWith(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")
'''
greetWith("Binh Vo", "chicago") # POSITIONAL Arguments

#Functions with keyword arguments - when switching the arguments 
#order around, it doesn't affect the position of the parameters, it doesn't matter
#since it knows which argument is assoociated with which parameter

greetWith(name="Binh", location="Chicago") 
greetWith(location="Chicago", name="Binh") 
'''

'''
83 - [Interactive Coding Exercise] Paint Area Calculator
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 x 4) ÷ 5 = 1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
'''
import math 
def paint_calc(height, width, cover):
    paintNeeded = math.ceil((height * width) / cover)
    print(f"You'll need {paintNeeded} cans of paint.")

'''
# 🚨 Tests👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
'''

'''
84 - [Interactive Coding Exercise] - Prime Number Checker
Definition of Prime: A prime number is a number that is divisible by one and itself. 
Prime numbers: 1 2 3 5 7 
'''
#Write your code below this line 👇
def primeChecker(number):
  # 4 % 4 = 0
  # 4 % 3 = 1
  # 4 % 2 = 0

  # 3 % 3 = 0
  # 3 % 2 = 1
  
  # 5 % 5 = 0
  # 5 % 4 = 1
  # 5 % 3 = 2
  # 5 % 2 = 1

  isPrime = False
  if number == 1 or number == 2:
    isPrime = True
  else:
    # loops through to check if the number is divisible by any other number
    for i in range(2, number):
      if number % i == 0:
        isPrime = False
        break
      else:
        isPrime = True
  
  if isPrime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

'''
n = int(input("Check this number: "))
primeChecker(number = n)
'''

def primeChecker2(number):
  isPrime = True

  for i in range(2, number):
    if number % 2 == 0:
      isPrime = False
      break

  if isPrime:
    print("It's a prime number.")
  else:
    print("It is not a prime number.")

