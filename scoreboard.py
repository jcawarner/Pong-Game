from turtle import Turtle


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()

		self.player_1 = 0
		self.player_2 = 0
		self.color("white")
		self.hideturtle()

	def create_scoreboard(self):
		self.penup()
		self.goto(0, 230)
		self.write(f"{self.player_1}   |   {self.player_2}", align="Center", font=("Arial", 40, "normal"))

	def player_1_score(self):
		self.clear()
		self.player_1 += 1
		self.write(f"{self.player_1}   |   {self.player_2}", align="Center", font=("Arial", 40, "normal"))

	def player_2_score(self):
		self.clear()
		self.player_2 += 1
		self.write(f"{self.player_1}   |   {self.player_2}", align="Center", font=("Arial", 40, "normal"))

	def game_over(self):
		self.home()
		if self.player_1 > self.player_2:
			self.write("GAME OVER\n Player 1 Wins!", align="Center", font=("Arial", 40, "normal"))
		else:
			self.write("GAME OVER\n Player 2 Wins!", align="Center", font=("Arial", 40, "normal"))