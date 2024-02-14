from turtle import *

bgcolor("gray") #sets background color

hideturtle() #hide the turtle while we move into the inital postion
penup() #don't draw during the move to the inital position
setpos(-300,0) #set starting position so we don't draw off the screen

color("yellow", "green") #set pen color yellow and fill color green
begin_fill() #fill all shapes drawn in the following code

for i in range(0,5): #loop starting each star 100 pixels away from it's origina point
    
    penup()
    forward(100)
    pendown()
    showturtle()
    
    for j in range (0,5): #loop turning right 144 degrees and moving forward 50 pixels 5 times to draw the star
        right(144)
        forward(50)
        
end_fill() #Everything drawn between being and end fill should be filled with the selected color 
           #Note that according to turtle the middle of the shape may not fill, which is the case for it's behavior on my machine.

done()