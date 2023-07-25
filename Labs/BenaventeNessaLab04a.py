# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: June 20, 2023
# Description: This is the first part of Lab 4. We will be drawing some simple objects using the graphics package. In this program the user will be prompted for several key object characteristics like size, shape, color, etc.
# Status: complete

# importing necessary packages

import graphics
import time

from graphics import *

# defining the main routine

def main():
    ### Moving a circle around another circle

        ### first we will set the name of the window to be the name of the b
        winName = input("What would you like the name of the window to be? ")

        ### now ask for a color. Note, only certain colors are valid (blue, green, yellow, red, etc)
        color1 = input("What color would you like the circle to be? ")

        ### now ask for the center coordinates of the circle. Recall that 'eval' will take the input and conver it to numbers
        x1,y1 = eval(input("What are the x,y coordinates for the center of the circle? "))

        ### now ask for the radius of the circle
        radius1 = eval(input("What is the radius of the circle? "))

        ### we now have all the input, so we can create the window object, the center of the 1st circle, and draw it
        win = GraphWin(winName, 500, 500)
        center1 = Point(x1,y1)
        circ1 = Circle(center1,radius1)
        circ1.setFill(color1)
        circ1.draw(win)

        ### next, we ask for the same information about the second circle, and draw it
        ### note how similar this is to the code above as we are creating a second circle here

        color2 = input("What color would you like the second circle to be? ")
        x2,y2 = eval(input("What are the x,y coordinates of the center of the circle? "))
        radius2 = eval(input("What is the radius of the circle? "))
        center2 = Point(x2,y2)
        circ2 = Circle(center2,radius2)
        circ2.setFill(color2)
        circ2.draw(win)

        ### we have 2 circles, the next thing to do is to draw a line between the centers of them
        ### recall that center1 is the center of the 1st circle, and center2 the center of the 2nd
        line = Line(center1,center2)

        ### set the color of the line to be red
        line.setFill('red')

        ### draw the line
        line.draw(win)

        ### this statement has the computer wait for a mouse click from the user
        ### on some systems this may only work with a left or right mouse click
        win.getMouse()

        ### this loop will now move the circle
        for i in range(10):
            ### we arbitrarily choe to move the circle 10 points in the x & y directions
            circ1.move(10,10)
            ### this gets rid of the line...it doesn't have to be in the loop!
            line.undraw()
            ### tell the computer to pause so that we can see the circle moving
            time.sleep(2)

        ### once we are done with the movement, query the center of the moved circle
        newCenter = circ1.getCenter()

        ### draw a new line from the center of the first circle to the center of the new circle
        line = Line(circ1.getCenter(), center2)
        line.setFill('red')
        line.draw(win)

        
                       
# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: June 20, 2023
# Description: This is the first part of Lab 4. We will be drawing some simple objects using the graphics package. In this program the user will be prompted for several key object characteristics like size, shape, color, etc.
# Status: complete

# importing necessary packages

import graphics
import time

from graphics import *

# defining the main routine

def main():
    ### Moving a circle around another circle

        ### first we will set the name of the window to be the name of the b
        winName = input("What would you like the name of the window to be? ")

        ### now ask for a color. Note, only certain colors are valid (blue, green, yellow, red, etc)
        color1 = input("What color would you like the circle to be? ")

        ### now ask for the center coordinates of the circle. Recall that 'eval' will take the input and conver it to numbers
        x1,y1 = eval(input("What are the x,y coordinates for the center of the circle? "))

        ### now ask for the radius of the circle
        radius1 = eval(input("What is the radius of the circle? "))

        ### we now have all the input, so we can create the window object, the center of the 1st circle, and draw it
        win = GraphWin(winName, 500, 500)
        center1 = Point(x1,y1)
        circ1 = Circle(center1,radius1)
        circ1.setFill(color1)
        circ1.draw(win)

        ### next, we ask for the same information about the second circle, and draw it
        ### note how similar this is to the code above as we are creating a second circle here

        color2 = input("What color would you like the second circle to be? ")
        x2,y2 = eval(input("What are the x,y coordinates of the center of the circle? "))
        radius2 = eval(input("What is the radius of the circle? "))
        center2 = Point(x2,y2)
        circ2 = Circle(center2,radius2)
        circ2.setFill(color2)
        circ2.draw(win)

        ### we have 2 circles, the next thing to do is to draw a line between the centers of them
        ### recall that center1 is the center of the 1st circle, and center2 the center of the 2nd
        line = Line(center1,center2)

        ### set the color of the line to be red
        line.setFill('red')

        ### draw the line
        line.draw(win)

        ### this statement has the computer wait for a mouse click from the user
        ### on some systems this may only work with a left or right mouse click
        win.getMouse()

        ### this loop will now move the circle
        for i in range(10):
            ### we arbitrarily choe to move the circle 10 points in the x & y directions
            circ1.move(10,10)
            ### this gets rid of the line...it doesn't have to be in the loop!
            line.undraw()
            ### tell the computer to pause so that we can see the circle moving
            time.sleep(2)

        ### once we are done with the movement, query the center of the moved circle
        newCenter = circ1.getCenter()

        ### draw a new line from the center of the first circle to the center of the new circle
        line = Line(circ1.getCenter(), center2)
        line.setFill('red')
        line.draw(win)

        
                       
