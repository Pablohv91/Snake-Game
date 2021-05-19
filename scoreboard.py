from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.contents = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-10, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        with open("High_score.txt") as self.file:
            self.contents = int(self.file.read())
            self.write(f"Score = {self.score} High Score {self.contents} ", align='center',
                       font=('Comic Sans MS', 12, 'normal'))

    def reset(self):
        if self.score > self.contents:
            with open("High_score.txt", 'w') as self.contents:
                self.contents.write(str(self.score))
                self.contents = self.score
        self.score = 0
        self.update_score()

    def add(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", align='center', font=('Arial', 24, 'normal'))
