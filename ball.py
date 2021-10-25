from turtle import Turtle



class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.x_cor = 10
		self.y_cor = 10


	def move(self):
		self.penup()
		new_x = self.xcor() + self.x_cor
		new_y = self.ycor() + self.y_cor
		self.goto(new_x, new_y)

	def bounce(self):
		self.y_cor *= -1


	def block(self):
		self.x_cor *= -1

	def new_round(self):
		self.hideturtle()
		self.home()
		self.showturtle()