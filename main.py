from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
score = Scoreboard()
score.create_scoreboard()


right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

right_paddle.create_paddle()
left_paddle.create_paddle()

ball = Ball()


screen.onkeypress(fun=right_paddle.move_up, key="Up")
screen.onkeypress(fun=right_paddle.move_down, key="Down")
screen.onkeypress(fun=left_paddle.move_up, key="w")
screen.onkeypress(fun=left_paddle.move_down, key="s")
screen.listen()
speed  = 0.1


is_game_true = True
while is_game_true:
	time.sleep(speed)
	ball.move()
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce()
	if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
		ball.block()
	if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
		ball.block()
	if ball.xcor() > 400:
		score.player_1_score()
		ball.new_round()
		speed -= 0.05
	if ball.xcor() < -400:
		score.player_2_score()
		ball.new_round()
	if score.player_1 >= 3 or score.player_2 >= 3:
		speed = 0.001
	elif score.player_1 >= 2 or score.player_2 >= 2:
		speed = 0.005
	elif score.player_1 >= 1 or score.player_2 >= 1:
		speed = 0.05
	if score.player_1 + score.player_2 == 10:
		ball.hideturtle()
		score.game_over()
		is_game_true = False

screen.exitonclick()