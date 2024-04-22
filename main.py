import random
import turtle
from turtle import Turtle, Screen
race = False
screen = Screen()

screen.title("Raphael Tutle racing")
screen.setup(width=500, height=400)

bet1 = screen.textinput("First User Enter your bet", "which win between Red, Blue, Green and Yellow Turtles Enter your names and bet ie # ma:black").lower()
bet2 = screen.textinput("Second User Enter your bet", "which win between Red, Blue, Green and Yellow Turtles Enter your names and bet ie # ma:black").lower()
bet3 = screen.textinput("Third User Enter your bet", "which win between Red, Blue, Green and Yellow Turtles Enter your names and bet ie # ma:black").lower()
bet4 = screen.textinput("Fourth User Enter your bet", "which win between Red, Blue, Green and Yellow Turtles Enter your names and bet ie # ma:black").lower()
bet1_info = bet1.split(":")
bet2_info = bet2.split(":")
bet3_info = bet3.split(":")
bet4_info = bet4.split(":")
name1 = bet1_info[0].title()
name2 = bet2_info[0].title()
name3 = bet3_info[0].title()
name4 = bet4_info[0].title()

betting1 = bet1_info[1]
betting2 = bet2_info[1]
betting3 = bet3_info[1]
betting4 = bet4_info[1]




Blue = Turtle(shape="turtle")
Blue.color("blue")
Blue.penup()
Red = Turtle(shape="turtle")
Red.color("red")
Red.penup()
Yellow = Turtle(shape="turtle")
Yellow.color("yellow")
Yellow.penup()
Green = Turtle(shape="turtle")
Green.color("green")
Green.penup()

Blue.goto(x=-230, y=160)
Red.goto(x=-230, y=60)
Green.goto(x=-230, y=-60)
Yellow.goto(x=-230, y=-160)


racers = [Red, Blue, Green, Yellow]

first = screen.numinput(title="race", prompt="hello", default=3)
second = screen.numinput(title="race", prompt=" Be ready", default=2)
third = screen.numinput(title="race", prompt="start", default=1)


if bet4:
    race = True

while race:

    for racer in racers:
        distance = random.randint(0, 10)
        racer.forward(distance)
        if racer.xcor() > 230:
            winning_color = (racer.pencolor())

            race = False
            if winning_color == betting1:
                print(f"The winner of the race is: {winning_color} so {name1} wins")
            if winning_color == betting2:
                print(f"The winner of the race is: {winning_color} so {name2} wins")
            elif winning_color == betting3:
                print(f"The winner of the race is: {winning_color} so {name3} wins")
            elif winning_color == betting4:
                print(f"The winner of the race is: {winning_color} so {name4} wins")

            else:
                print("no one wins the race")



















































screen.exitonclick()
