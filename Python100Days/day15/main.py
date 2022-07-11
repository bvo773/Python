from pickle import FALSE


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_machine_running = True

def report():
  print("COFFEE MACHINE STATUS")
  for resource in resources:
    print (f"{resource}: {resources[resource]}")
  print()

def check_resources(ingredients)-> bool:
  for ingredient in ingredients:
    if resources[ingredient] < ingredients[ingredient]:
      return False
  return True

def deduct_resources(ingredients)-> None:
    for ingredient in ingredients:
      ingredient_cost = ingredients[ingredient]
      resources[ingredient] = resources.get(ingredient) -  ingredient_cost

def process_coins()-> int:
  print("Please insert coins")
  quarters = int(input("how many quarters?: ")) * .25
  dimes = int(input("how many dimes?: ")) * .10
  nickels = int(input("how many nickels? ")) * .05
  pennies = int(input("how many pennies? ")) * .01
  total = quarters + dimes + nickels + pennies
  return total

while coffee_machine_running:
  choice = input("What would you like? (espresso/latte/cappucino/off/report): ")
  if choice == "off":
    coffee_machine_running = False
  elif choice == "report":
    report()
  else:
    cost = MENU[choice]["cost"]
    ingredients = MENU[choice]["ingredients"]
    cx_amount = process_coins()
  
    if cx_amount < cost:
      print("Sorry, that's not enough money. Money refunded")
    else:
      if check_resources(ingredients):
        deduct_resources(ingredients)
        change = round(cx_amount - cost,2)
        resources["Money"] = round(resources.get("Money", 0) + cx_amount - change,2)
        print(f"Here is ${change} in change.\n")
      else:
        print("Sorry not enough resources in coffee machine.")
