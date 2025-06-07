from turtle import Turtle,Screen

"""Imported all related modules n classes"""

ALIGN='center'
FONT=('Arial',20,'normal')

"""Constants"""

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,210)
        self.hideturtle()
        self.screen=Screen()
        self.User_choice=0

    """selection of level of difficulty by user"""

    def difficulty(self):
        flag=True
        while flag:
            self.User_choice=self.screen.textinput("Choose your difficulty", "1-easy/2-medium/3-hard")
            if not isinstance(int(self.User_choice),int):
                flag=True 
                continue
            flag=False
        self.update_scoreboard()

    """Updating scores on scoreboard"""

    def update_scoreboard(self):
        self.write(f"Level of difficulty: {self.User_choice},Score: {self.score}",align=ALIGN,font=FONT)

    """Gameover popup"""

    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over!!!!! ",align=ALIGN,font=FONT)

    """Increasing score when the snake eats food"""
    
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
        
