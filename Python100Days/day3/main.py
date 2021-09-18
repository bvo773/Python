'''
DAY 3 TOPICS - CONDITIONAL STATEMENTS | LOGICAL OPERATORS| CODE BLOCKS | SCOPE
'''

# 26 - Control Flow - IF/ELSE Statement and Conditional Operators
'''
if condition:
    do this
else:
    do this

COMPARISON OPERATORS
Operator
    >  | greater than
    <  | less than
    >= | great than or equal to
    <= | less than or equal to
    == | equal to
    != | not equal to
'''
def watchRatedRMovies():
    age = int(input("Age: "))
    if (age > 18):
        print("You can watch rated R movies")
    else:
        print("Sorry you are underage")

'''
28 - Write a program that works out whether if a given number is an odd or even number 
'''
def exercise1():
    num = int(input("What number do you want to check? "))
    if (num % 2 == 0):
        print("This is an even number")
    else:
        print("This is an odd number")


'''
29 - Nested if statements and elif statements
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
'''

def nestedIfElse():
    height = int(input("Height in cm? "))
    if (height > 120):
        print("You can ride the rollercoaster")
        age = int(input("Age: "))
        if (age >= 18):
            print("Your ticket is $12")
        else:
            print("Your ticket is $7")
    else:
        print("Sorry you can't ride the rollercoaster, too short")

'''
if/elfif/else statements - Check all conditions until one is false
if condition 1:
    do A
elif condition 2:
    do B
else
    do this
'''
def nestedIfElse():
    height = int(input("Height in cm? "))
    if (height > 120):
        print("You can ride the rollercoaster")
        age = int(input("Age: "))
        if (age >= 12 and age <= 18):
            print("Please pay $7")
        elif (age > 18):
            print("Please pay $12")
        else:
            print("Please pay $5")
    else:
        print("Sorry you can't ride the rollercoaster, too short")

'''
30 - Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value. Round results to whole number
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

Formula: BMI = weight(kg)/ [height(m)]^2
'''
def exercise2():
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))

    bmi = round(weight / (height ** 2))
    if (bmi < 18.5): print(f"BMI: {bmi}, underweight")
    elif (bmi < 25): print(f"BMI: {bmi}, normal weight")
    elif (bmi < 30): print(f"BMI: {bmi}, slightly overweight")
    elif (bmi < 35): print(f"BMI: {bmi}, obese")
    else: print(f"{bmi}, clinically obese")


'''
31 - Write a program that works whether a given year is a leap year 
on every year that is divible by 4
    except every year is divisible by 100
        unless the year is divisible by 400
'''

def isLeapYear():
    year = int(input("Year: "))
    if (year % 4 == 0):
        if (year % 100 == 0):
            if(year % 400 == 0):
                print (f"{year} is a leap year")
            else:
                print (f"{year} not leap year")
        else:
            print(f"{year} is leap year")  
    else: 
        print(f"{year} not leap year")
isLeapYear()