from turtle import *

name = ""

while name != None:
      name =textinput("Name","Please enter your name: ")
      if name == None:
        break
      
      elif name!=None:
          write(name)
          penup()
          right(90)
          forward(25)
          left(90)
          pendown()

done()