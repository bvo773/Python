'''
DAY 5 - FOR LOOPS, RANGE, AND CODE BLOCKS
PROJECT - PASSWORD GENERATOR with letters, symbols, and numbers
ITERABLE - an iterable such as list, tuple, set, dictionary, etc.
'''

'''
50 - Using For Loop with Python Lists
Loop allows to execute the same line of code multiple times
for item in list_of_items:
  #Do somthing to each item
'''
def forloop():
  fruits = ["Apple", "Peach", "Pear"]
  # taking the list fruits and use the var fruit to assign to each item in fruits
  for fruit in fruits: 
    print(fruit)
    print(fruit + " Pie")

'''
51 - [Interactive Coding Exercise] Average Height
RULES: CANNOT use Python functions: sum(iter) and len(list)
FORMAT:
		for item in itemList:
				# do something for each item
INSTRUCTIONS:
You are going to write a program that calculates the average student height from a List of heights.
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
e.g.
180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572
Average height rounded to the nearest whole number = 164
'''
def averageStudentHeights():
  studentHeights = input("Input a list of student heights cm: ").split()
  for num in range(0, len(studentHeights)):
    studentHeights[num] = int(studentHeights[num])

  studentTotal = 0
  heightTotal = 0
  for height in studentHeights:
    heightTotal += height
    studentTotal += 1

  averageHeight = round(heightTotal/studentTotal)
  print(f"There are total of {studentTotal} heights at an average of {averageHeight} cm.")

def averageStudentHeights2():
  studentHeights = input("Input a list of student heights: ").split()
  for n in range(0, len(studentHeights)):
    studentHeights[n] = int(studentHeights[n])

  heightTotal = sum(studentHeights)
  studentTotal = len(studentHeights)

  averageHeight = round(heightTotal/studentTotal)
  print(f"There are total of {studentTotal} heights at an average of {averageHeight} cm.")

'''
52 - [Interactive Coding Exercuse] HIGH SCORE
RULES: CANNOT use Python functions: max(iterable), min(iterable)
'''
def findMaxScore():
  studentScores = input("Input a list of student scores: ").split()
  for n in range(0, len(studentScores)):
    studentScores[n] = int(studentScores[n])
		
  maxScore = 0
  for score in studentScores:
    if score > maxScore:
        maxScore = score

  print(studentScores)
  print("The highest score is: " + str(maxScore))

'''
53 - for loops and range() function
# Sometimes we might want to use a loop completely 'independent' of a list
CARL GAUSS GENIUS EXERCISE: ADD ALL the numbers from 1 TO 100
He flipped the numbers around, add the two lines = 101, there are 50 pairs of 101 = 5050 GENIUS
1   + 2  +  3 + ... + 98 + 99 + 100
100 + 99 + 98 + ... + 3  + 2  + 1

- Can shorten this with the range function: range(start,stop,step)
- Use range function if you want to generate a range of numbers to loop throug

SYNTAX:
for number in range(start, end, step): #[inclusive-exclusive)
				print(number) #each number in that range do something with that number
'''
def rangeforloop():
  #for num in range(1,11): # 1 - 10
  #	print(num)

  #for num in range(1,11,3): # 1-4-7-10
  #	print(num)

  #GAUSS game more efficient than 2 mins haha
  total = 0
  for num in range(1,101):
      total += num
  print(total)

'''
54 - [Interactive Coding Exercise] ADDING EVEN NUMBERS from 1-100
'''
def addEvenNumbers():
  evenSum = 0
  for num in range(1, 101):
    if num % 2 == 0:
      evenSum += num
	
  evenSum2 = 0
  for num in range(2, 101, 2):
    evenSum2 += num
  
  print(f"Even Sum Total 1-100: {evenSum} | {evenSum2}")


'''
55 - CODING EXERCISE FIZZBUZZ
- You are going to write a program that automatically prints the solution to the FizzBuzz game.
- Your program should print each number from 1 to 100 in turn
- When the number is divisible by 3 then instead of printing the number it should print "Fizz".
- `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
- `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

`1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz`
'''
def fizzBuzz():
  for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0):
      print('FizzBuzz')
    elif number % 3 == 0:
      print('Fizz')
    elif number % 5 == 0:
      print('Buzz')
    else:
      print (number)


'''
56 - Day 5 Project password generator
'''
def passwordGenerator():
  #Password Generator Project
  import random
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  print("Welcome to the PyPassword Generator!")
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  #Eazy Level - Order not randomised:
  #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
  password = ""
  for l in range(0, nr_letters):
    password += letters[random.randint(0, len(letters) - 1)]
    # password += random.choice(letters)

  for s in range(0, nr_symbols):
    password += symbols[random.randint(0, len(symbols) - 1)]
    # password += random.choice(symbols)

    
  for n in range(0, nr_numbers):
    password += numbers[random.randint(0, len(numbers) - 1)]
    # password += random.choice(numbers)


  print("Easy password: " + password)
  # print(type(password))
  #Hard Level - Order of characters randomised:
  #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
  passwordList = []
  for c in password:
    passwordList.append(c)

  print(f"Before shuffle: {passwordList}")
  random.shuffle(passwordList)
  print(f"After shuffle: {passwordList}")

  hardPassword = "".join(passwordList)
  '''
  shorter syntax to join each item from a list into an empty string 
  instead of creating an empty string and cocatenate each char into the string
  password = ""
  for char in passworList
    password += char
  '''


  print("Hard password: " + hardPassword)


passwordGenerator()