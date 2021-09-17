# Functions can be resused and imported to other parts of your program
# A function definition...
# def functionName():
#   blockOfCode

# A method signature: method name + paramaters

def helloWorld():
    print("Hello World")

def computeArea(length, width):
    area = length * width
    print(area)

def findMaxium(firstNumber, secondNumber):
    if (firstNumber > secondNumber):
        print("First number is greater")
    elif (secondNumber > firstNumber):
        print("Second number is greater")
    else:
        print("Both numbers are equal")
        
    
    
def main():
    helloWorld()
    computeArea(5, 7)
    
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))
    findMaxium(firstNumber, secondNumber)

if __name__ == "__main__":
    main()