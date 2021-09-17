'''
DAY 1 TOPICS - PRINTING | COMMENTING | STRING MANIPULATION | VARIABLES
'''
print("Hello World")
print("Printing \"Binh Vo\" in quotation")


def exercise1():
    print("Day 1 - Python Print Function")
    print("The function is declared like this: ")
    print("print('what to print')")

# Debugging String Practice - 8
def exercise2():
    print("Day 1 - String Manipulation")
    print("String Concatenation is done with the \"+\" sign.")
    print("e.g. print(\"Hello \"" + " + " + "\"world\")")
    print("New lines can be created with a backslash and n.")

def exercise2s():
    print("Day 1 - String Manipulation")
    print('String Concatenation is done with the "+" sign.')
    print('e.g. print("Hello " + "world")')
    print("New lines can be created with a backlash and n")

# The Python input function - 9 | 10
def user_input():
    print("Hello " + input("What is your name?"))

def exercise3():
    print(len(str(input())))

# Variables - 11 | 12 | Switching variables values
def exercise4():
    a = input("a: ")
    b = input("b: ")

    temp_a = a
    a = b
    b = temp_a

    print("a: " + a)
    print("b: " + b)

def project_brand_name_generator():
    # Greetings for the program
    print("Hello, program for a brand name")
    # Ask user city
    city = input("What city do you live in?\n")
    # Ask user for the name of a pet
    pet = input("What is your pet name?\n")
    # Combine name of city and pet for brand name
    print("Brand name: " + city + " " + pet)

project_brand_name_generator()