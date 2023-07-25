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
    if celsius < -20:
        print("The temperature is very cold. Bundle up!")
    elif -20 <= celsius < 0:
        print("The temperature is quite cold.")
    elif 0 <= celsius < 15:
        print("The temperature is cool.")
    elif 15 <= celsius < 25:
        print("The temperature is moderate.")
    elif 25 <= celsius < 30:
        print("The temperature is warm. Don't forget to stay hydrated!")
    else:
        print("The temperature is hot. Sunscreen is necessary!")

def main():
    try:
        f = float(input("What is the Fahrenheit temperature? "))
        c = calc_celsius(f)
        output_data(c)
    except ValueError:
        print("Invalid input. Please enter a valid Fahrenheit temperature as a number.")

main()

