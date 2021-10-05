def turn_right():
    turn_left()
    turn_left()
    turn_left()

# check for a right path while we moving straight    
def hop():
    turn_right()
    move()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        while(front_is_clear()):
            move()
            if not wall_on_right():
                hop()
    elif wall_on_right() and wall_in_front():
        turn_left()
    else:
        move()