from turtle import *

hideturtle()
penup()
setpos(-300,0)

for i in range(0,5):
    
    penup()
    forward(100)
    pendown()
    showturtle()
    
    for j in range (0,5):
        right(144)
        forward(50)

done()