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
if/elfif/else statements - Check all conditions until one is false, unless if 1 condition is true, only that condition is carried out
if condition 1:
    do A
elif condition 2:
    do B
else
    do this
'''
def if_elif_else():
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

FLOW CHART
            [START]
               |
    NO    (year / 4?)     YES
    |                      |
    |                      |
 [Not leap year]   NO   (year/100?)  YES
                   |                  | 
                   |                  |
                [Leap year]    NO (year/400?) YES
                               |              |
                               |              |
                        [Not leap year]     [Leap Year]
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

'''
32 - Multiple if statements in sucession | check all conditions, only execute conditions that are true
FLOW CHART
                                    [START]
                                       |
                                 no-(height>120)-yes
                                 |                |
                            [cant ride]      <12-(age)------
                                              |    |<12-18 | >18 age
                                            [+5]   |       |
                                              |   [+7]    [+12]
                                              |    |       |
                                           no |____|_______|yes
                                        no|--(want photos?)--yes
                                          |_______            |
                                                  |         [+3]
                                                  |           |
                                             [The total bill is $x] 


'''

def multipleIf():
    height = int(input("Height cm: "))
    if(height > 120):
        print("Can ride")
        age = int(input("Age: "))
        cost = 0
        if (age < 12):
            cost += 5
        elif (age <= 18):
            cost  += 7
        else:
            cost += 12
        
        wantPhotos = str(input("Want photos? y/n? "))
        if (wantPhotos == 'y'):
            cost += 3
        
        print(f"The total bill is ${cost}")
    else:
        print("Can't ride")

def multipleIfV():
    height = float(input('Height (ft.in): '))

    if (height > 4):
        age = int(input("Age: "))
        bill = 0
        if (age < 12):
            bill += 5
        elif (age >= 12 and age <= 18):
            bill += 7
        else:
            bill += 12
        
        wantPhotos = str(input("Want photos(y/n)? "))

        if(wantPhotos == 'y'):
            bill += 3
        print(f"Total bill is {bill}")

    else:
        print("Sorry you cant ride")

'''
33 - Write a program to calculate the bills of the pizza (Practice multiple ifs statements)
small pizza - 15
medium pizza - 20
large pizza - 25
pepperoni for small pizza - 2
pepperoni for medium or large pizza - 3
extra cheese for any pizza - 1
'''
def exercise4():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size do you want? S, M, or L: ")
    addPepperoni = input("Do you want pepperoni? Y or N: ")
    addCheese = input("Do you want to add cheese? Y or N: ")

    bill = 0
    if (size == "S"):
        bill += 15
    elif (size == "M"):
        bill += 20
    else:
        bill += 25
    
    if (addPepperoni == "Y"):
        if (size == "S"):
            bill += 2
        else:
            bill += 3
    
    if (addCheese == "Y"):
        bill += 1

    print("Your final bill is: " + str(bill)) 

'''
35 - Logical Operators to check for "multiple conditions"
if condition1 & condition2 & condition3:
    do this
else:
    do this

Logical AND: (A and B) | both A and B have to be true for the condition to be true
Logical OR:  (A or  B) | Either A or B has to be true or both A and B for the condition to be true
Logical NOT not(E) | Reverse the condition -> if condition true, not(condition) -> false (vice versa)
Eg. for Logical not
x = 12
x > 14 -> False
not (x>14) -> True
'''
def logicalOperators():
    height = int(input("Height cm: "))
    if(height > 120):
        print("Can ride")
        age = int(input("Age: "))
        cost = 0
        if (age < 12):
            cost += 5
        elif (age >= 12 and age < 18):
            cost += 7
        elif (age >= 18 and not(age >= 45 and age <=55)):
            cost += 12
        else:
            print("Your age is classified as midlife crisis, have a free ride on us")
        
        wantPhotos = str(input("Want photos? y/n? "))
        if (wantPhotos == 'y'):
            cost += 3
        
        print(f"The total bill is ${cost}")
    else:
        print("Can't ride")  

'''
35 - Love Calculator
Suggestive functions: lower(), count()
Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 
`name1 = "Angela Yu"`

`name2 = "Jack Bauer"`

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times
'''
def loveCalculator():
    name1 = str(input("Name of person 1: ")).lower()
    name2 = str(input("Name of person 2: ")).lower()

    combined_names = name1 + name2
    trueCount = 0
    loveCount = 0 

    trueCount += combined_names.count("t")
    trueCount += combined_names.count("r")
    trueCount += combined_names.count("u")
    trueCount += combined_names.count("e")
    
    loveCount += combined_names.count("l")
    loveCount += combined_names.count("o")
    loveCount += combined_names.count("v")
    loveCount += combined_names.count("e")


    score = str(trueCount) + str(loveCount)
    numScore = int(score)
    if (numScore < 10 or numScore > 90):
        print(f"Your score is {score}, you go together like coke and mentos")
    elif (numScore >= 40 and numScore <= 50):
        print(f"Your score is {score}, you are alright together")
    else:
        print(f"Your score is {score}")

loveCalculator()