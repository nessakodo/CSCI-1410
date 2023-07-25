# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: June 20, 2023
# Description: This is the second part of lab 4. Applying the principles learned in part 1, we will draw 2 circles, and move one around the other 90 degrees upon each click within the window.
# Status: complete

# importing necessary packages

import math
from graphics import *

# defining the main route -- moving a circle around another circle

def main():
    winName = "Lab 4 - BenaventeNessa"
    win = GraphWin(winName, 500, 500)

    # here we will ask the user where and how the first circle will be drawn
    
    color1 = input("What color would you like the circle to be? ")
    x1, y1 = eval(input("What are the x, y coordinates for the center of the circle? "))
    radius1 = eval(input("What is the radius of the circle? "))

    # now we will draw the first circle
    
    center1 = Point(x1, y1)
    circ1 = Circle(center1, radius1)
    circ1.setFill(color1)
    circ1.draw(win)

    # this second circle will take into account the specifications of the 2nd part of the lab below
    # the center of circle two uses the formula x2=x1, y2 = y1-(2*r1)), we will make this easier by defining distance

    color2 = "green"
    radius2 = radius1 / 2
    distance = 2 * radius1
    x2 = x1
    y2 = y1 - distance
    center2 = Point(x2, y2)

    # now lets draw the second circle
    
    circ2 = Circle(center2, radius2)
    circ2.setFill(color2)
    circ2.draw(win)

    # and the connecting red line!
    
    line = Line(center1, center2)
    line.setFill('red')
    line.draw(win)


    # for the final part of the lab, we will use this loop to move the second circle and red line 90 degrees to the right every time the user clicks the window

    while True:
        win.getMouse()

        angle = math.radians(90)
        dx = (center2.getX() - center1.getX()) * math.cos(angle) - (center2.getY() - center1.getY()) * math.sin(angle)
        dy = (center2.getX() - center1.getX()) * math.sin(angle) + (center2.getY() - center1.getY()) * math.cos(angle)
        new_center2 = Point(center1.getX() + dx, center1.getY() + dy)

        circ2.move(new_center2.getX() - center2.getX(), new_center2.getY() - center2.getY())
        line.undraw()
        line = Line(center1, new_center2)
        line.setFill('red')
        line.draw(win)

        center2 = new_center2

    win.close()

main()
