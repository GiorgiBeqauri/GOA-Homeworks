# ეს არის სტრინგი
print("giorgi beqauri")
# ეს არის ინტეჯერი
print(5)

# ეს არის სტრინგი
print("5")


# ეს არის float
print(5.0)



# error
print(5 + "asdsad")
# სწორია
print(5 + int("5"))

print(float(5))


print("giorgi beqauri aris" + str(13) + "wlis")


from turtle import *

# Setu
speed(2)
penup()
goto(-100, -100)
pendown()

# Draw the base of the house
begin_fill()
color("blue")
forward(200)  # Bottom
left(90)
forward(200)  # Right side
left(90)
forward(200)  # Top
left(90)
forward(200)  # Left side
end_fill()

# Draw the roof
begin_fill()
color("red")
goto(-100, 100)  # Left corner of the roof
goto(0, 200)     # Top point of the roof
goto(100, 100)   # Right corner of the roof
goto(-100, 100)  # Back to start
end_fill()


exitonclick()