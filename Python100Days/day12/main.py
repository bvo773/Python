'''
116 - NAMESPACES: LOCAL VS GLOBAL SCOPE
Local scope exists within FUNCTIONs
Global scope exists outsides Functions, anything can access the global defined vars
The Difference between local and global scope where you define or where you create your variables or your functions
Namespace: Anything that we defined(variable, function, class, etc) has a namespace and that namespace is valid in certain scopes
'''
#################### Scope ###############
enemies = 1

def increase_enemies():
  enemies = 2 # this vari
  print(f"enemies inside function {enemies}")

increase_enemies()
print(f"enemies outside function {enemies}")

# Local Scope
def drink_potion():
  potion_strength = 2
  print(potion_strength)
drink_potion()
#print(potion_strength) -> would return an nameerror since its scope is within the drink_potion() function and it is not defined 

# Global Scope
# Example 1)
player_health = 10
def drink_medication():
  print(player_health)

drink_medication()

# Example 2)
nums = [1,2,3]
def modify_nums(arr):
  arr[0] = 4
  print(f"arr:{arr}")
  print(f"nums:{nums}")

# Example 3)
player_health = 10
def game():
  def drink_potion():
    potion_strength = 2
    print(player_health)
  
  drink_potion()

'''
117 - Block Scope: PYTHON does not have block scope like Java, C++
Block statements (any sort of block of code that's indented) (":") - if, else, for, while. There is no offense.
  - If a variable is created within a block statement, it still has the same scope as its enclosing function
  - Or if there is no enclosing function, it would be global scope

OVERALL - If you create a variable within a function, it's only available within that function
but if you create a variable within an if block or a while loop or a for loop or anything that has the indentation and colon,
then it does count create a speparate local scope. 
'''
game_level = 3
enemies = ["Skeleton","Zombie", "Alien"]
if game_level < 5:
  new_enemy = enemies[0] # choose easy enemy

print(new_enemy) # perfectly valid code -> skeleton

def create_enemy():
  enemies = ["Skeleton","Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies[0]
  
  print(new_enemy)

'''
118 - How to Modify a Global Variable, avoid modifying global scope, like modifying it inside a function
'''
enemies = 1
def increase_enemies():
  global enemies 
  enemies += 1

# instead of modifying enemies, we can access it global scope and add 1 and return it
def increase_enemies():
  return enemies + 1

total_enemy = increase_enemies()
print(total_enemy)
print(enemies)

''' 
119 - PYTHON CONSTANTS AND GLOBAL SCOPE 

Global Scope are useful when defining constants. Global constants. 
'''

# Global Constants - Variable that you define and you're never planning to change it again. Like the value of pi
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@deewbit"