import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import Score
screen=Screen()
screen.setup(650,650)
screen.title("snake game")
screen.bgcolor("black")
x=0
snake=[]
sn=Snake()
f=Food()
s=Score()

screen.tracer(0)
game=True
screen.listen()

screen.onkey(sn.up,"Up")
screen.onkey(sn.down,"Down")
screen.onkey(sn.left,"Left")
screen.onkey(sn.right,"Right")

while game == True:
     screen.update()
     time.sleep(0.1)
     game2=sn.move()
     if not game2:
         s.high_score()
         sn.restart()
     if sn.head.distance(f)<15:
         f.refresh()
         s.sc()
         sn.add_snake()
     for seg in sn.snake[1::1]:
         if sn.head.distance(seg)<10:
             sn.restart()
             s.high_score()






screen.exitonclick()
