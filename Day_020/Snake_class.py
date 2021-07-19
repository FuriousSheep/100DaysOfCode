import turtle as t
from math import isclose


class Snake:
    def __init__(self):
        self.CASE_SIZE = 20
        self.body = self.make()
        self.head = self.body[0]

    def new_part(self):
        """Creates a single block to be added to the snake body"""
        snake_part = t.Turtle()
        snake_part.shape("square")
        snake_part.penup()
        snake_part.color("#FAFAFA", "#232323")
        return snake_part

    def make(self):
        """Initialises the snake by creating and placing three blocks on the screen"""
        snake = []
        for i in range(0, 3):
            snake_part = self.new_part()
            snake_part.setx(snake_part.xcor() - self.CASE_SIZE * i)
            snake.append(snake_part)
        return snake

    def move(self):
        """Moves the entire snake following its head"""
        snake_length = len(self.body)
        for i in range(0, snake_length - 1):
            # We start at the tail of the snake, and move it where the next snake
            # part is, repeat to where we get to the last part before the head
            tail_index = snake_length - i - 1
            self.body[tail_index].setpos(self.body[tail_index - 1].pos())
        self.body[0].forward(self.CASE_SIZE)

    def set_listeners(self, screen):
        """Sets the listeners for the snake movement"""
        screen.onkey(key="Up", fun=self.turn_north)
        screen.onkey(key="Down", fun=self.turn_south)
        screen.onkey(key="Left", fun=self.turn_west)
        screen.onkey(key="Right", fun=self.turn_east)
        screen.listen()

    def turn_north(self):
        """Turns head north"""
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def turn_south(self):
        """Turns head south"""
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def turn_east(self):
        """Turns head east"""
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def turn_west(self):
        """Turns head west"""
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def is_dead(self):
        """Returns true if snake is either out of bounds or has collided with itself, 
        otherwise returns false"""
        x = self.head.xcor()
        y = self.head.ycor()
        out_of_bounds = x > 300 or x < -300 or y > 300 or y < -300

        collided = False
        snake_length = len(self.body)
        for i in range(1, snake_length):
            same_x = isclose(self.head.xcor(), self.body[i].xcor())
            same_y = isclose(self.head.ycor(), self.body[i].ycor())
            collided = same_x and same_y
            if collided:
                return True
        return out_of_bounds
