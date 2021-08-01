from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Pick your turtle race color: ")
color_choices = ['red', 'yellow', 'green', 'blue', 'pink', 'purple']
x = -230
y = 200
all_turtles = []
is_game_on = False

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color_choices[i])
    new_turtle.penup()
    new_turtle.speed('fastest')
    y = y - 50
    new_turtle.goto((x, y))
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for i in all_turtles:
        random_distance = random.randint(0,10)
        i.forward(random_distance)

    if i.xcor() > 230:
        is_game_on = False
        winning_color = i.pencolor()

        if user_bet == winning_color:
            print(f"You've won! The {winning_color} is the winner")
        else:
            print(f"You've lost! The {winning_color} is the winner")


screen.exitonclick()
