from turtle import Turtle,Screen
positions=[(0,0),(-20,0),(-40,0)]
import time
screen=Screen()
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.snake = []
        self.x=0
        self.create_snake()
        self.head = self.snake[0]
    def create_snake(self):
        for pos in positions:
            self.extended(pos)

    def extended(self,pos):
        self.tom = Turtle(shape="square")
        self.tom.up()
        self.tom.color("white")
        self.tom.speed(10)
        self.tom.goto(pos)
        self.snake.append(self.tom)


    def add_snake(self):
        self.extended(self.snake[-1].position())

    def move(self):
        game=True
        for i in range(len(self.snake) - 1, 0, -1):
                new_x = self.snake[i - 1].xcor()
                new_y = self.snake[i - 1].ycor()
                self.snake[i].goto(new_x, new_y)
                if self.snake[0].xcor()>290:
                     game=False
                elif self.snake[0].ycor()>290:
                     game=False
                elif self.snake[0].xcor()<-290:
                      game=False
                elif self.snake[0].ycor()<-290:
                     game=False
        self.snake[0].forward(20)
        return game
    def up(self):
        if self.snake[0].heading()!=DOWN:
             self.snake[0].setheading(90)
    def down(self):
        if self.snake[0].heading() != UP:
              self.snake[0].setheading(270)
    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(0)
    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(180)

    def restart(self):
         for i in self.snake:
            i.goto(1000,1000)
         self.snake.clear()
         self.create_snake()
         self.head=self.snake[0]
