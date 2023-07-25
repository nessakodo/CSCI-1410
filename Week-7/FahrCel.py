################################################################
#
# Write a program that converts temperatures from Fahrenheit to Celsius.
#
# Analysis
#   The temperature is given in Fahrenheit, user wants it expressed in
#   degrees Celsius.
#
# Specifications
#   Input – temperature in Fahrenheit
#   Output – temperature in Celsius
#   Output = (input - 32) * (5/9)
################################################################

def main():

    
    f = eval(input("What is the Fahrenheit temperature? "))
    
    c = (f - 32) * (5/9)

    print("The temperature is", c, "degrees Celsius.")

