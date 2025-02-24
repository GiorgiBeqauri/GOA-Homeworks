from turtle import *

speed(9)
width(5)
penup()
goto(-100, -100)
pendown()

# Draw the base of the house
begin_fill()
color("blue")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

# Draw the roof
begin_fill()
color("red")
goto(-100, 100)
goto(0, 200)
goto(100, 100)
goto(-100, 100) 
end_fill()

# Draw the left window
penup()
goto(-70, 0)
pendown()
begin_fill()
color("white")
forward(30) 
left(90)
forward(30)
left(90)
forward(30) 
left(90)
forward(30)
end_fill()

# Draw the right window
penup()
goto(40, 0)
pendown()
begin_fill()
color("white")
forward(30)
left(90)
forward(30) 
left(90)
forward(30) 
left(90)
forward(30) 
end_fill()


exitonclick()