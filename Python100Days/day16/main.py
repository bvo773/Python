"""
DAY 1-15 - Procedural Programming, we set up procedures and functions that do particular things. One procedure leads to another procedure.
DAY 16 - Object Oriented Programming, we should maintain one to one relationship as our code gets complex
  - Modules can be reuse
  - Splitting tasks into different classes to break down its functionality
  - OOP is trying to model a real world object.
  - Object has attributes and methods
  - We can create objects by defining a class type of it
  - Thus, the blueprint lets us create many objects we want from this define class type

class Waiter:
  #attributes
  is_holding_plate = True
  tables_responsible = [4,5,6]

  #methods - We call it method b/c its a function that a particular modeled object can do.
  def take_order(table,order):
    #takes order to chef
  
  def take_payment(amount):
    #add money to restaurant

#Object    Class
  car  =  CarBlueprint()
"""
import another_module
print(another_module.another_variable)

#using module turtle(Turtle Graphic Library) to construct our Turtle object
#import turtle
#bino = turtle.Turtle()
from turtle import Turtle, Screen
bino = Turtle()
print(bino)
bino.shape("turtle")
bino.color("green")
bino.forward(100)

# Constructing screen object and using its attributes
my_screen = Screen()
print(my_screen.canvheight)
# accessing the screen object method
my_screen.exitonclick()