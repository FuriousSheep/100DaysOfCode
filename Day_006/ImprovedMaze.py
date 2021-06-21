#https://reeborg.ca/reeborg.html, now with edge cases handled!

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def solve_maze():
    turn_count = 0
    while not at_goal():
        if wall_on_right():
            turn_count = 0
            if front_is_clear():
                move()
            else:
                turn_left()
        else:
            if not turn_count == 4:
                turn_right()
                move()
                turn_count+=1
            else:
                turn_count = 0
                if front_is_clear():
                    move()
                else:
                    turn_left()
                    
