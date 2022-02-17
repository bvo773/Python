'''
DAY 2 TOPICS - UNDERSTANDING DATA TYPES | NUMBERS | OPERATIONS | TYPE CONVERSION | f-String
'''

# 19 Python Primitive Data Types (String, Integer, Float, Boolean) 
from email import message


def py_data_types():
  #String - text of characters
  print("Hello"[0]) #subscript - pull particular element from the string
  print("Hello"[1]) # -> e printed out
  print("Hello"[4]) # -> o printed out
  print("123" + "456") # concat the strings together

  #Integer - whole number, no decimal
  print(123 + 456) # add two integers together
  print(123_456_789) # large int naming convention

  #Float - decimal or float data type
  print(3.14159)

  #Boolean
  True
  False


# 20 Type Error, Type Checking and Type Conversion(Type Casting)
def type_error():
	name_length = len(input("What is your name?"))
	print(type(name_length))
	print("Your name has " + name_length + " characters") # TypeError: int object


def type_conversion():
	name_length = len(input("What is your name? ")) # len() returns int value
	name_str_length = str(name_length) #convert int object to str object using str()
	print("Your name has " + name_str_length + " characters")

def typeConversionB():
  name_length = len(input("What is your name? "))
  print("Your name has " + str(name_length) + " characters.")

def type_conversion2():
	print(70 + float("100.5")) #convert string to float and add it to int
	print(str(773) + str(855)) #convert ints to strs and concat them

# 21 [Interactive Coding Exercise] Add digits in a two digit number, HINT: get the subscript of the string at 0 and 1 | convert to int objects | add them
def exercise1():
	two_digit_number = input("Two digit num: ")
	print(type(raw_num))
	digit_1 = int(raw_num[0])
	digit_2 = int(raw_num[1])
	print(digit_1 + digit_2)

# Arithmetic operations in Python, follow PEMDAS - 20
# PEMDAS Left to Right|() -> ** -> * -> / -> + -> -
def math_operations():
	print(6/3) # Division return-> float obj
	print(3 + 5)
	print(6 - 2)
	print(4 * 2)
	print(2 ** 3) # exponent 2^3
	print(3 * 3 + 3 / 3 - 3) # PEMDAS -> returns a float obj
	print(3 + 3 + 3 - 3 - 3)
	print((3 * 3) / 3 - 3 + 3)

	
# 23 [Interactive Coding Exercise] BMI Calculator 
def bmi_calculator():
  # 🚨 Don't change the code below 👇
  height = input("enter your height in m: ")
  weight = input("enter your weight in kg: ")
  # 🚨 Don't change the code above 👆

  #Write your code below this line 
  bmi = int(int(weight)/float(height) ** 2)
  #bmi = round(numWeight/(numHeight ** 2))
  print(bmi)

# 24 :) NUMBER MINUPULATION(round()) and F strings in Python  |
def number_manipulate():
  print(8/3)
  print(round(8/3)) # 2.666666665 -> 3
  print(round(8/3,2)) # round 2 dec places -> 2.67
  print(8 // 3) # floor division to get an integer -> 2
  print(type(8//3)) # return int object not float

  result = 4/2
  result /= 2 # result = result / 2 | works with any operations(* / + -)
  print(result)

	# using f strings to convert ALL DATA TYPES into a STRING instead of using str() to convert each data type
  height = 5.7
  weight = 155
  isOverWeight = False
  print(f"Binh's height is {height} ft. He weights {weight} pounds. Is he overweight? {isOverWeight}")

# 25 [Interactive coding exercise] Life in Weeks: Create a program f- strings to tell us how many days, weeks, months we have left until 90 years old
  '''
  age = 25
  remaningYears = 90 - 25 = 65 years
  12 m = 1 yr
  65 y * 12 m 

  52 weeks = 1 yr
  52 weeks * 65 y

  365 d = 1 yr
  365 d * 65 y
  '''

def life_until_ninety():
  age = input("What is your current age? ")
  years_remaining = 90 - int(age)
  
  months_remaining = (years_remaining * 12)
  weeks_remaining = (years_remaining * 52)
  days_remaining = (years_remaining * 365)

  message = f"You have {months_remaining} days, {weeks_remaining} weeks, {days_remaining} months left."
  print(message)

life_until_ninety()

# 26 Project TIP Calculator  - FORMAT STRING FUNCTION
'''If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
'''

def tipCalculator():
	print("Welcome to the tip calculator")
	totalBill = float(input("What is the total bill? "))
	tipPercent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
	totalSplit = int(input("How many people to split the bill? "))

	tipPercent = (tipPercent/100) + 1
	costPerPerson = round((totalBill/totalSplit) * tipPercent, 2)
	print(f"Each person should pay: {costPerPerson}")

	#print 2 decimal places with 0
	print("(With 0) Each person should pay {:.2f}".format(costPerPerson)) # PRINTING 2 DECIMAL PLACES WITH format()
		
def tipCalculatorB():
  #If the bill was $150.00, split between 5 people, with 12% tip. 

  #Each person should pay (150.00 / 5) * 1.12 = 33.6
  #Format the result to 2 decimal places = 33.60

  #Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

  #Write your code below this line 👇

  print ("Welcome to the tip calculator!")
  totalBill = float(input("What is the total bill? "))
  tipPercentage = int(input("How much tip would you like to give up? 10, 12, or 15? "))
  totalPeople = int(input("How many people to split the bill? "))

  amountPerPerson = (totalBill * (1 + tipPercentage/100)) / totalPeople
  formatAmountPerPerson = "${:.2f}".format(amountPerPerson) # Using str.format() to format the float with two decimal places and returns it as a string
  print (f"Each person should pay: {formatAmountPerPerson}")