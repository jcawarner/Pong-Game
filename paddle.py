from turtle import Turtle

class Paddle(Turtle):

	def __init__(self, x_pos, y_pos):
		super().__init__()


		self.shape("square")
		self.x_pos = x_pos
		self.y_pos = y_pos

	def create_paddle(self):
		self.penup()
		self.turtlesize(stretch_wid=5, stretch_len=1)
		self.color("white")
		self.goto(self.x_pos, self.y_pos)



	def move_up(self):
		self.y_pos += 10
		self.goto(self.x_pos, self.y_pos)

	def move_down(self):
		self.y_pos -= 10
		self.goto(self.x_pos, self.y_pos)
