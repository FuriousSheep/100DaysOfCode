from turtle import Turtle

SCORE_HEIGHT = 260


class Score():
    def __init__(self, xoffset):
        self.score = 9
        self.height = SCORE_HEIGHT
        self.xoffset = xoffset
        self.blocks = {}
        self.block_keys = list("ABCDEFG")
        self.fill_blocks()
        self.setup_blocks()
        self.resize_blocks()
        self.hide_blocks()
        self.zero()

    def create_block(self):
        block = Turtle()
        block.penup()
        block.shape("square")
        block.color("white")
        return block

    def fill_blocks(self):
        for key in self.block_keys:
            self.blocks[key] = self.create_block()

    def setup_blocks(self):
        blocks_pos = [
            (-10, 10),
            (0, 20),
            (10, 10),
            (0, 0),
            (-10, -10),
            (0, -20),
            (10, -10),
        ]
        # print(self.blocks)
        i = 0
        for letter in self.block_keys:
            self.blocks[letter].setx(self.xoffset + blocks_pos[i][0])
            self.blocks[letter].sety(self.height + blocks_pos[i][1])
            i += 1

    def resize_blocks(self):
        for key in self.block_keys[::2]:
            self.blocks[key].shapesize(1.5, 0.5)
        for key in self.block_keys[1::2]:
            self.blocks[key].shapesize(0.5, 1.5)

    def hide_blocks(self):
        for key in self.block_keys:
            self.blocks[key].ht()

    # Show numbers

    def zero(self):
        for key in ["A", "B", "C", "E", "F", "G"]:
            self.blocks[key].showturtle()

    def one(self):
        for key in ["C", "G"]:
            self.blocks[key].showturtle()

    def two(self):
        for key in ["B", "C", "D", "E", "F"]:
            self.blocks[key].showturtle()

    def three(self):
        for key in ["B", "C", "D", "F", "G"]:
            self.blocks[key].showturtle()

    def four(self):
        for key in ["A", "C", "D", "G"]:
            self.blocks[key].showturtle()

    def five(self):
        for key in ["A", "B", "D", "F", "G"]:
            self.blocks[key].showturtle()

    def six(self):
        for key in ["A", "B", "D", "E", "F", "G"]:
            self.blocks[key].showturtle()

    def seven(self):
        for key in ["B", "C", "G"]:
            self.blocks[key].showturtle()

    def eight(self):
        for key in ["A", "B", "C", "D", "E", "F", "G"]:
            self.blocks[key].showturtle()

    def nine(self):
        for key in ["A", "B", "C", "D", "F", "G"]:
            self.blocks[key].showturtle()

    def update_score(self):
        self.score += 1
        if self.score > 9:
            return
        self.hide_blocks()
        [
            self.zero,
            self.one,
            self.two,
            self.three,
            self.four,
            self.five,
            self.six,
            self.seven,
            self.eight,
            self.nine,
        ][self.score]()
