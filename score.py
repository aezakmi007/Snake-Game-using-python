from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highest_score.txt') as file:
           self.high_score  = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreBoard()
        self.hideturtle()

    def update_scoreBoard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", align='center', font=("Arial", 20, "normal"))

    def reset(self):
        if int(self.score) > self.high_score:
            self.high_score = str(self.score)
            with open('highest_score.txt', mode='w')as file:
              file.write(str(self.score))
        self.score = 0
        self.update_scoreBoard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.wrtie("GAME OVER", align = 'center', font)

    def increase_score(self):
        self.score += 1
        self.update_scoreBoard()