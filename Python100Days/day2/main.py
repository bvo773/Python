'''
DAY 2 TOPICS - DATA TYPES | NUMBERS | OPERATIONS | TYPE CONVERSIO | f-String
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

# BMI Calculator. Create a calculator to calculate the Body Mass Index (BMI) from a user's weight and height | Form: BMI = weight(kg)/height^2(m^2)
# Person A - 160 pounds 6'0 | Person B - 160 pounds 5'0 | Even though they are both same weight, person B is overweight since he is shorter
def exercise2():
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))
    
    bmi = int(weight/(height ** 2))
    print("Your BMI: " + str(bmi))

exercise2()
