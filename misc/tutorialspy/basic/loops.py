
# 1) for loop executes a block of statements in sequence #
# for variable in sequence 
fruits = ["apple", "orange", "banana"]
for fruit in fruits:
    print(fruit)
# range()
for number in range(1,5):
    print(number, end = ' ') #print 1,2,3,4
print("\n") # 'print' newline and 'go' to newline


# 2) while loop executes a block of statements if a certain condition is true #
temperature = 75
while (temperature >= 68 and temperature <= 75): # Executes statements if condition is true: 68-75
    print("Room temperature is maintained {} degree fahrenheit".format(temperature))
    temperature -= 1

print() #nl

# 3) infinite while loop by having the condition as "True" #
# while True:
#    print ("Running forever")

# 4) nested while loops: loop within a loop #
# Matrix [m x n]: m - iteration of 'outer' for loop, n - iterator of 'inner' for loop
# Matrix [2 x 3]: For each iteration of the outer for loop, the inner loops executes 3 times
#   1 2 3 
#   4 5 6
#   7 8 9
number = 1
for row in range(1, 4):
    for column in range(1,4):
        print(number, end = ' ') # Add a space at the end of each print statement, doesn't go to newline
        number += 1 # increment the number so it doens't print the same number twice
    print() # print a new line to go onto the next row

print() #nl

# 5) Break, Continue statements
# a) break - stop the loops from further executing based on a certain condition
print("Print the numbers, if number is 4 --> Break ")
for number in range(1,6): # 1-5
    if (number == 4):
        break
    else:
        print(number, end = ' ')
print() # nl
# b) continue - skip a 'particular iteration' based on a certain condition and continue to execute the statements
print("Print the numbers, if number is 4 --> Continue(Skip!) it")
for number in range(1,6):
    if (number is 4):
        continue
    else:
        print(number, end = ' ')