'''
DAY 1 TOPICS - PRINTING | COMMENTING | STRING MANIPULATION | VARIABLES
'''
print("Hello World")
print("Printing \"Binh Vo\" in quotation")


def exercise1():
	print("Day 1 - Python Print Function")
	print("The function is declared like this: ")
	print("print('what to print')")

# 9 String Manipulation - (newlines, concatenation)
def exercise1a():
  # use \n to print new line
  print("Hello world!\nHello world!\nHello world!")
  print("Example) Hello" +  " " + "Binh")

# 10 [Interactive coding exercise] Debugging Pratice 
def exercise2b():
  print("Day 1 - String Manipulation")
  print("String Concatenation is done with the \"+\" sign.")
  print('e.g. print("Hello " + "world")')
  print("New lines can be created with a backslash and n.")

def exercise2c():
	print("Day 1 - String Manipulation")
	print('String Concatenation is done with the "+" sign.')
	print('e.g. print("Hello " + "world")')
	print("New lines can be created with a backlash and n")

# 11 The Python input() function -> input("A prompt for the user")
def user_input():
	print("Hello " + input("What is your name?"))

# 12 [Interactive Coding Exercise] Input function - Calculating the length of an input string
def exercise3():
  print(len(str(input())))

def exercise3b():
  print( len( input("What is your name? ") ) )

# 13 Python Variables | # 14 [Interactive Coding Exercises] Switching variables values
def exercise4():
	a = input("a: ")
	b = input("b: ")

	temp = a
	a = b
	b = temp

	print("a: " + a)
	print("b: " + b)

# 15 Variable Naming
# Make your code readable and it makes sense to you

# 16 Day 1 Project: Band Name Generator 
def project_band_name_generator():
  # Greetings for the program
  print("Hello, program for a brand name")
	# Ask user city
  city = input("What city do you live in?\n")
	# Ask user for the name of a pet
  pet = input("What is your pet name?\n")
	# Combine name of city and pet for brand name
  print("Band name: " + city + " " + pet)

def project_band_name_generator2():
  #1. Create a greeting for your program.
  print("Welcome to the Band Name Generator")
  #2. Ask the user for the city that they grew up in.
  city = input("What is the city name you grew up in?\n")
  #3. Ask the user for the name of a pet.
  pet = input("What is your pet name?\n")
  #4. Combine the name of their city and pet and show them their band name.
  print("Your band name could be " + city + " " + pet)
  #5. Make sure the input cursor shows on a new line

project_band_name_generator2()
