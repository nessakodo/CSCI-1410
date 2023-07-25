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
    try:
        f = float(input("What is the Fahrenheit temperature? "))
        c = (f - 32) * (5/9)
        print("The temperature is", c, "degrees Celsius.")
    except ValueError:
        print("Invalid input. Please enter a valid Fahrenheit temperature as a number.")

main()
