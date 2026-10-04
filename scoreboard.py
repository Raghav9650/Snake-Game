from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(arg=f"Score: {self.score}",align="center",font=("Aerial",24,"normal"))
        self.hideturtle()
        self.update_scoreboard()
  
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High score: {self.highscore}",align="center",font=("Aerial",24,"normal"))
    
    def increase(self):
        self.score+=1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER!!!!!",align="center",font=("Aerial",45,"normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")

        self.score=0
        self.update_scoreboard()
