from turtle import *
speed(30)
width(4)
# დავხაზოთ კვადრატი
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

# დავხაზოთ კარები
forward(70)
color("gray")
begin_fill() # შიგნით გაფერადება
left(90)
forward(120) # კარების სიმაღლე
right(90)
forward(60)
right(90)
forward(120) 
end_fill()

penup() # კალმის აღება
goto(200, 200)
pendown() # კალმის ჩამოწევა

# დავხაზოთ სახურავი
color("red")
begin_fill() # შიგნით გაფერადება
right(150)
forward(200)
left(120)
forward(200)
end_fill() # გაფერადება დასრულებულია

#დავხაზოთ ფანჯარა
color("black")
left(30)
forward(70)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(20)
#დავხაზოთ მეორე ფანჯარა
right(90)
forward(200)
right(90)
forward(20)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

exitonclick()