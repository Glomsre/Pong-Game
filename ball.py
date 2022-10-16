from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        #questo di sotto (new_y)diventa negativo quando moltiplicato per -1
        #nella funzione sotto bounce
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def restart_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        #qui è dove tocca le barre , riduciamo il timesleep
        self.move_speed *= 0.9
        #0.1 * 0.9 = 0.09 e cosi via







