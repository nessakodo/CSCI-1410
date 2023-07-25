# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: June 20, 2023
# Description: This is lab 3. It asks users the dimensions of the box and calculates the number of segments of trim needed to go around the box, plus the cost and the amound of money lost due to not being able to buy the trim in segments less than 12".
# Status: complete

import math

def main():
    #first ask the user for the dimensions of their box
    l=float(input("Enter the length of your box "))
    w=float(input("Enter the width of your box "))

    #formula to calculate the perimiter of the box
    perimiter=2*(l+w)

    #formulas to calculate the number of segments of trim needed both as a float and int
    trim=perimiter/12
    tFloat=float(trim)
    tInt=int(math.ceil(trim))
    
    #formula to calculate the cost of the trim
    unitCost=1.88
    totalCost=tInt*unitCost
    
    #formula to calculate the amount of money lost due to only being able to buy 12" increments
    wasteInches=(tInt-tFloat)*12
    wasteCost=(wasteInches)*(unitCost/12)
    
    #finally print the output for all of the above inputs and formulas
    print("Thank you, it appears your box has a perimiter of " ,perimiter , "inches.")
    print("You will need to buy " ,tInt , "trim boards.")
    print("This will cost $" ,format(totalCost,".2f"),".")
    print("You will waste" ,format(wasteInches,".2f"), "inches of trim, which equates to a waste of $",format(wasteCost,".2f"),".")

    
main()
