'''
Program: Double Arrow
Filename: doubleArrow-tRaj-00.py
Author: Tushar Raj
Description: Exactly recreate the "double-arrow" figure shown in question with the exact dimensions
Revisions: No revisions made
'''

import turtle #Access the Turtle module
#There are no literal constraint
#There are no class defined
#There are no functions defined
canvas = turtle.Screen() #Establish a drawing window
tom =  turtle.Turtle() #create a tom object

#Announce
print("****Double Arrow****");
print("Exactly recreating the double-arrow figure along with same dimentions\n")

### moving the turtle to the location from where it has to start creating
tom.left(90) #moves the turtle's pointer by 90 degree left
tom.penup() #this function pick up the pen so the when turtle moves it dosent draw on screen
tom.forward(50) #this moves the turtle by 50 in the direction turtle is pointing

### Starts drawing the double arrow
tom.pendown() #this function put down the pen so the when turtle moves it start drawing on screen again
tom.right(90) #moves the turtle's pointer by 90 degree right
tom.forward(100) #moves the turtle's by 100,drawling line on the screens
tom.left(90) #moves the turtle's pointer by 90 degree left
tom.forward(50) #moves turtle by 50
tom.right(135) #moves the turtle's pointer by 135 degree right
tom.forward(141.1) #moves turtle by 141.1
tom.right(90) #moves the turtle's pointer by 90 degree right
tom.forward(141.1) #moves turtle by 141.1
tom.right(135) #moves the turtle's pointer by 135 degree right
tom.forward(50) #moves turtle by 50
tom.left(90) #moves the turtle's pointer by 90 degree left
tom.forward(200) #moves turtle by 200
tom.left(90) #moves the turtle's pointer by 90 degree left
tom.forward(50) #moves turtle by 50
tom.right(135) #moves the turtle's pointer by 135 degree right
tom.forward(141.1) #moves turtle by 141.1
tom.right(90) #moves the turtle's pointer by 90 degree right
tom.forward(141.1) #moves turtle by 141.1
tom.right(135) #moves the turtle's pointer by 135 degree right
tom.forward(50) #moves turtle by 50
tom.left(90) #moves the turtle's pointer by 90 degree left

###Completes the drawing of the double arrow figure
tom.forward(100) #moves turtle by 100
tom.right(90) #moves the turtle's pointer by 90 degree right

### Moving the turtle to the same place where it started
tom.penup() #this function pick up the pen so the when turtle moves it dosent draw on screen
tom.forward(50) #moves turtle by 50
tom.pendown() #this function put down the pen so the when turtle moves it start drawing on screen again
tom.left(90) #moves the turtle's pointer by 90 degree left

### End of Double arrow program
print("****Double Arrow program ended****")
