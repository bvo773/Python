'''
Day 18 - Turtle Graphics, Tuples and Importing Modules
    Random facts
        - turtle module uses tkinter(gui) under the hood to create the graphics
PROJECT: Generating a million dollar piece of artwork Damien Hirst.
Using Turtle Graphics, we can use a turtle with a pen on its back and everywhere it goes, it leaves a trail of line
'''

from turtle import Turtle, Screen
from multiprocessing import Process
import random


# Setting up turtle and decorating it
aceu_the_turtle = Turtle()
aceu_the_turtle.shape("turtle") #change it to a turtle shape
aceu_the_turtle.color("LightCoral")


colors = ["LightCoral","aquamarine", "DeepSkyBlue2","Pink", "white"]

# each time it walks, it picks a random color, a random one of the 4 directions:
def draw_random_walk(turtle):
    for i in range(100):
        position = turtle.pos()
        if position[0] < -300 or position[0] > 300:
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
        elif position[1] < -300 or position[1] > 300:
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
        draw_patterns(turtle,i)

def another_direction(turtle):
    turns = random.randint(0, 4)
    for _ in range(turns):
        turtle.left(90)

def draw_patterns(turtle, cur_num):
    turtle.color(random.choice(colors))
    turtle.pensize(random.randint(1,5))
    turtle.speed(random.randint(7,20))
    turtle.pendown()
    if cur_num % 2 == 1:
        another_direction(turtle)
        turtle.forward(random.randint(5, 25))
    else:
        turtle.forward(random.randint(5,25))


def draw_shape(turtle, num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

def draw_different_shapes(turtle):
    turtle.penup()
    turtle.goto(random.randint(-200, 200), random.randint(-200,200))
    turtle.color(random.choice(colors))
    turtle.pensize(random.randint(1,4))
    turtle.speed(random.randint(2,7))
    for i in range(3, 6):
        turtle.color(random.choice(colors))
        turtle.pendown()
        draw_shape(turtle, i)
    
def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

def draw_dashed_line(turtle):
    turtle.penup()
    turtle.goto(random.randint(-200, 200), random.randint(-200,200))
    turtle.color(random.choice(colors))
    turtle.pensize(random.randint(1,4))
    turtle.speed(random.randint(2,7))
    for _ in range(random.randint(10, 40)):
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        

def sound():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("holdon.wav")
    pygame.mixer.music.play()

# Initialize, and begin calling functions here
screen = Screen()
screen.bgcolor("black")

sound()
for _ in range(20):
    # draw_square(aceu_the_turtle)
    # draw_y(aceu_the_turtle)
    # draw_o(aceu_the_turtle)
    # draw_dashed_line(aceu_the_turtle)
    
    draw_different_shapes(aceu_the_turtle)
    draw_random_walk(aceu_the_turtle)
    draw_dashed_line(aceu_the_turtle)



screen.exitonclick() #our window doesn't dissapear until we click on it
