def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# START!

while (not at_goal()):
    jump()




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
