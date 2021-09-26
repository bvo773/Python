'''
DAY 2 TOPICS - UNDERSTANDING DATA TYPES | NUMBERS | OPERATIONS | TYPE CONVERSIO | f-String
'''

#Python Primitive Data Types (String, Integer, Float, Boolean) - 17 
def py_data_types():
	#String - text of characters
	print("Hello"[0]) #subscript - pull particular element from the string
	print("Hello"[4]) # -> o printed out
	print("123" + "456")

	#Integer - whole number, no decimal
	print(123 + 456)
	print(123_456_789) # large int naming convention

	#Float - decimal or float data type
	print(3.14159)

	#Boolean
	True
	False

#Type Error, Type Checking and Type Conversion - 18
def type_error():
	name_length = len(input("What is your name?"))
	print(type(name_length))
	print("Your name has " + name_length + " characters") # TypeError: int object

def type_conversion():
	name_length = len(input("What is your name? "))
	name_str_length = str(name_length) #convert int object to str object using str()
	print("Your name has " + name_str_length + " characters")

def type_conversion2():
	print(70 + float("100.5")) #convert string to float and add it to int
	print(str(773) + str(855)) #convert ints to strs and concat them

#Add digits in a two digit number, get the subscript of the string at 0 and 1 | convert to int objects | add them
def exercise1():
	raw_num = input("Two digit num: ")
	print(type(raw_num))
	digit_1 = int(raw_num[0])
	digit_2 = int(raw_num[1])
	print(digit_1 + digit_2)

# Arithmetic operations in Python, follow PEMDAS - 20
# PEMDAS L-R|() -> ** -> * -> / -> + -> -
def math_operations():
	print(6/3) # Div -> float obj
	print(3 + 5)
	print(6 - 2)
	print(4 * 2)
	print(2 ** 3) # exponent 2^3
	print(3 * 3 + 3 / 3 - 3) # PEMDAS -> returns a float obj
	print(3 + 3 + 3 - 3 - 3)
	print((3 * 3) / 3 - 3 + 3)

	
	#bmi = int(weight/(height ** 2))
	#print("Your BMI: " + str(bmi))

# NUMBER MINUPULATION(round()) and F strings in Python - 22 |
def number_manipulate():
	print(round(8/3)) # 2.666666665 -> 3
	print(round(8/3,2)) # round 2 dec places -> 2.67
	print(8 // 3) # floor division -> 2
	print(type(8//3)) # return int object not float

	result = 4/2
	result /= 2 # result = result / 2 | works with opeprations(* / + -)
	print(result)

	# using f strings to convert all data types into a string instead of using str() to convert each data type
	height = 5.7
	weight = 155
	isOverWeight = False
	print(f"Binh's height is {height} ft. He weights {weight} pounds. Is he overweight? {isOverWeight}")

	# Life in Weeks: Create a program f- strings to tell us how many days, weeks, months we have left until 90 years old
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
def lifeInWeeks():
	age = input("What is your current age? ")
	remainingYears = 90 - int(age)

	months = (remainingYears * 12)
	weeks = (remainingYears * 52)
	days = (remainingYears * 365)

	print(f"You have {days} days, {weeks} weeks, {months} months left.")

	#Project TIP Calculator - 22 - FORMAT STRING FUNCTION
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
		
