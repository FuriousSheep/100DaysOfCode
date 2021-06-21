# https://reeborg.ca/reeborg.html Hurdles 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    while front_is_clear():
        move()
    jump()
