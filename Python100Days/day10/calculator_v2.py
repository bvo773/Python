def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# storing function in a dictionary 
# key: symbol | value: name of function
# 'Hey Python, see this variable? It will take a function, but don't call it yet(do make it run)."
# like this:

# operations={
# '+':add,
# '-':subtract
# }
# meaning you stored a bunch of adresses to functions without calling any, without runnning them.

# and as soon as you want to, you can call them by saying:
# answer=operations['+'](1,1)
# function = operations["*"]
# function(2,3)/
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
from art import logo

def calculator():
  print(logo)
  num1 = float(input("What is the first number? "))

  for symbol in operations:
    print(symbol)

  shouldContinue = True

  while shouldContinue:
    operationSymbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    calculationFunction = operations[operationSymbol]
    answer = calculationFunction(num1, num2)

    print(f"{num1} {operationSymbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
      num1 = answer
    else:
      shouldContinue = False
      calculator()

calculator()