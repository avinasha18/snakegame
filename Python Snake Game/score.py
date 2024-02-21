from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        file=open("scoredata.txt",)
        self.highest=int(file.read())
        file.close()
        self.score=0
        self.hideturtle()
        self.up()
        self.color("white")
        self.goto(0, 290)
        self.write(f"score:{self.score} High score:{self.highest}",align="center",font=("Arial",20,"normal"))

    def update_score(self):
        self.clear()
        self.write(f"score:{self.score} High score:{self.highest}", align="left", font=("Arial", 20, "normal"))
    def sc(self):
        self.score+=1
        self.update_score()


    def high_score(self):
        if self.score>self.highest:
            self.highest=self.score
            file1=open("scoredata.txt","w")
            file1.write(str(self.score))

        self.score=0
        self.update_score()
