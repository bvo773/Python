from art import logo
print(logo)
num1 = float(input("What's the first number?: "))
print("+\n-\n*\n/ ")
def calculate(num1, num2, operation):
  if operation == "+":
    total = float(round(num1 + num2))
    print(f"{num1} {operation} {num2} = {total}")
    return total
  elif operation == "-":
    total = float(round(num1 - num2))
    print(f"{num1} {operation} {num2} = {total}")
    return total
  elif operation == "*":
    total = float(round(num1 * num2))
    print(f"{num1} {operation} {num2} = {total}")
    return total
  elif operation == "/":
    total = float(round(num1 / num2))
    print(f"{num1} {operation} {num2} = {total}")
    return total

continueCalculating = True
while continueCalculating:
  operation = input("Pick an operation: ")
  num2 = float(input("What's the next number?: "))
  result = calculate(num1,num2, operation)

  choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'e' to end: ").lower()

  if choice == 'y':
    continueCalculating = True
    num1 = result
  elif choice == 'n':
    from replit import clear
    clear()
    print(logo)
    print("+\n-\n*\n/ ")
    num1 = float(input("What's the first number?: "))
  elif choice == 'e':
    print("Terminating program... Good Bye...")
    continueCalculating = False
