from turtle import Turtle,Screen

ALIGN='center'
FONT=('Arial',20,'normal')

class Scoreboard(Turtle):
    """This creates the scoreboard and updates the score"""
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,210)
        # self.hideturtle()
        self.screen=Screen()
        self.User_choice=0

    def difficulty(self):
        """selection of level of difficulty by user"""
        flag=True
        while flag:
            self.User_choice=self.screen.textinput("Choose your difficulty", "1-easy/2-medium/3-hard")
            if not isinstance(int(self.User_choice),int):
                flag=True 
                continue
            flag=False
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updating scores on scoreboard"""
        self.write(f"Level of difficulty:{self.User_choice} Score: {self.score}",align=ALIGN,font=FONT)

    def gameover(self):
        """Gameover popup"""
        self.goto(0,0)
        self.write(f"Game Over!!!!! ",align=ALIGN,font=FONT)
    
    def increase_score(self):
        """Increasing score when the snake eats food"""
        self.score+=1
        self.clear()
        self.update_scoreboard()
        
