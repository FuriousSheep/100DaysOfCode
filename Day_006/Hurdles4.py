#https://reeborg.ca/reeborg.html Hurdles4

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    while wall_in_front():
        turn_left()
        move()
        turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()

