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

def output_data(fahrenheit):
    celsius = calc_celsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit is {celsius} degrees Celsius.")

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

def read_temp(temperature_list):
    for f in temperature_list:
        output_data(f)

def get_temperature_list():
    try:
        num_temperatures = int(input("How many temperatures do you want to convert? "))
        temperature_list = []
        for i in range(num_temperatures):
            f = float(input(f"Enter temperature {i+1} in Fahrenheit: "))
            temperature_list.append(f)
        return temperature_list
    except ValueError:
        print("Invalid input. Please enter valid Fahrenheit temperatures as numbers.")

def main():
    temperature_list = get_temperature_list()
    if temperature_list:
        read_temp(temperature_list)

main()
