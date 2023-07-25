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

def calc_celsius(fahrenheit):
    return round((fahrenheit - 32) * (5/9), 2)

def output_data(celsius):
    # Modify this function as per your desired output or processing
    print("The temperature is", celsius, "degrees Celsius.")

def main():
    try:
        f = float(input("What is the Fahrenheit temperature? "))
        c = calc_celsius(f)
        output_data(c)
    except ValueError:
        print("Invalid input. Please enter a valid Fahrenheit temperature as a number.")

main()

