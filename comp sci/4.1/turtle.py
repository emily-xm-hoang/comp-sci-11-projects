"""Mini-Assignment 3
## Mini-Assignment 3 "Gotta Have" Checklist (10 / 10)

- Well done, although there are just barely enough comments- a top-level comment describing what the program does overall would be helpful.

- [X] Code runs: Program executes with the Run button.

- [X] Functionality (2 points): Makes use of the following python turtle functions: penup()/pendown() (at least once each), goto(x, y) (at least 3 times), stamp() (at least once), and circle(radius) (at least twice)

- [X] Interactivity: User input is used for an interactive drawing

- [X] While loop: Contains a while loop

- [X] Function: Defines and uses your own function

- [X] Theme: Drawing fits a theme

- [X] Algorithm Design/comments/testing: Algorithm written in English prior to coding. Comments for at least each key section of code (e.g. each part being drawn). Comment in the header describes a key example demonstrating that the program works

- [X] Code Organization: Code is clean and well-organized

- [X] Submission: Code is committed and synced to Github in a file at 4.1/turtle.py
"""

import turtle # imports turtle module
joe = turtle.Turtle() # creates a turtle
turtle.colormode(255)
# turtle.Screen().bgcolor(102, 193, 238)
joe.speed(0)
joe.hideturtle()
user = input("What colour is the sky? ")
turtle.Screen().bgcolor(user)

while True:
    command = input("There is no turning back...\nWould u like to proceed? (yes, no) ").strip(" ,.!?").lower()
    if command == "no":
        break
    elif command == "yes":
        # hill
        joe.penup()
        joe.goto(0, -1150)
        joe.pendown()
        joe.color(121, 186, 87)
        joe.fillcolor(121, 186, 87)
        joe.begin_fill()
        joe.circle(550)
        joe.end_fill()

        # sun
        joe.penup()
        joe.goto(120, 130)
        joe.pendown()
        joe.color(252, 231, 88)
        joe.fillcolor(255, 249, 168)
        joe.begin_fill()
        joe.pensize(5)
        joe.circle(20)
        joe.end_fill()
        joe.penup()
        joe.goto(95, 125)
        joe.pendown()
        joe.setheading(230)
        joe.forward(7)
        joe.penup()
        joe.goto(135, 120)
        joe.pendown()
        joe.setheading(279)
        joe.forward(7)
        joe.penup()
        joe.goto(155, 150)
        joe.pendown()
        joe.setheading(-30)
        joe.forward(7)
        joe.penup()
        joe.goto(135, 120)
        joe.pendown()
        joe.setheading(279)
        joe.forward(7)
        joe.penup()
        joe.goto(148, 176)
        joe.pendown()
        joe.setheading(30)
        joe.forward(7)
        joe.penup()
        joe.goto(125, 185)
        joe.pendown()
        joe.setheading(89)
        joe.forward(9)
        joe.penup()
        joe.goto(100, 180)
        joe.pendown()
        joe.setheading(135)
        joe.forward(8)
        joe.penup()
        joe.goto(90, 160)
        joe.pendown()
        joe.setheading(173)
        joe.forward(7)

        # main body of the house
        joe.pensize(1)
        joe.penup()
        joe.goto(-80,-55)
        joe.pendown()
        joe.fillcolor(255, 242, 197)
        joe.color(255, 242, 197)
        joe.begin_fill()
        joe.setheading(0)
        for i in range(4):
            joe.forward(150)
            joe.left(90)
        joe.end_fill()

        # triangle yellow part of the house
        joe.penup()
        joe.goto(70,95)
        joe.pendown()
        joe.setheading(135)
        joe.begin_fill()
        joe.forward(90)
        joe.setheading(225)
        joe.forward(110)
        joe.end_fill()
        joe.penup()

        # roof
        joe.penup()
        joe.goto(-80, 95)
        joe.pendown()
        joe.color(201, 139, 91)
        joe.fillcolor(249, 153, 107)
        joe.setheading(45)
        joe.begin_fill()
        joe.forward(90)
        joe.setheading(0)
        joe.forward(22)
        joe.setheading(225)
        joe.forward(90)
        joe.end_fill()
        joe.penup()
        joe.goto(-72, 96)
        joe.pendown()
        joe.setheading(45)
        joe.forward(90)
        joe.penup()
        joe.goto(-64, 96)
        joe.pendown()
        joe.setheading(45)
        joe.forward(90)
        def draw_tiles(x, y):
            joe.setheading(273)
            joe.penup()
            joe.goto(x,y)
            joe.pendown()
            for i in range(2):
                joe.circle(3, 180)
                joe.circle(-3, 180)
        draw_tiles(-25, 150)
        draw_tiles(-35, 140)
        draw_tiles(-45, 130)
        draw_tiles(-55, 120)
        draw_tiles(-65, 110)
        draw_tiles(-75, 100)

        # antenna
        joe.pensize(2)
        joe.penup()
        joe.goto(-10, 155)
        joe.pendown()
        joe.color(0, 0, 0)
        joe.setheading(90)
        joe.forward(40)
        joe.penup()
        joe.goto(-25, 187)
        joe.pendown()
        joe.setheading(9)
        joe.forward(27)
        joe.penup()
        joe.goto(-17, 180)
        joe.pendown()
        joe.setheading(9)
        joe.forward(15)

        # random line going down the middle of the house
        joe.penup()
        joe.goto(-57, 95)
        joe.pendown()
        joe.color(226, 216, 162)
        joe.setheading(270)
        joe.forward(150)

        # door
        joe.penup()
        joe.goto(-74,-55)
        joe.pendown()
        joe.fillcolor(254, 231, 146)
        joe.setheading(0)
        joe.begin_fill()
        door = [10, 60, 10, 60]
        for sides in door:
            joe.forward(sides)
            joe.left(90)
        joe.penup()
        joe.goto(-67,-25)
        joe.pendown()
        joe.circle(1)
        joe.end_fill()

        # windows
        def draw_window(x, y):
            joe.pensize(2)
            joe.penup()
            joe.goto(x, y)
            joe.pendown()
            joe.color(255, 255, 255)
            joe.fillcolor(136, 205, 239)
            joe.begin_fill()
            joe.setheading(0)
            for i in range(4):
                joe.forward(30)
                joe.left(90)
            joe.end_fill()
            joe.penup()
            joe.goto(x+15, y)
            joe.pendown()
            joe.left(90)
            joe.forward(30)
            joe.penup()
            joe.goto(x, y+15)
            joe.pendown()
            joe.setheading(0)
            joe.forward(30)
        draw_window(-35, 50)
        draw_window(25, 50)
        draw_window(25, -20)
        draw_window(-35, -20)

        joe.penup()
        joe.goto(-74, 50)
        joe.pendown()
        joe.begin_fill()
        funny_window = [10, 30, 10, 30]
        for number in funny_window:
            joe.forward(number)
            joe.left(90)
        joe.end_fill()
        joe.penup()
        joe.goto(-69, 50)
        joe.pendown()
        joe.left(90)
        joe.forward(30)
        joe.penup()
        joe.goto(-74, 65)
        joe.pendown()
        joe.setheading(0)
        joe.forward(10)

        turtle.done() # keeps the window open
    else:
        import random
        x = random.choice(range(-500,500))
        y = random.choice(range(-500,500))
        joe.goto(x,y)
        joe.stamp()
        print("bruh, try again")
