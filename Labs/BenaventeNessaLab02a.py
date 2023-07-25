# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: June 13, 2023
# Description: This is lab 2. It takes in a temperature in Fahrenheit and converts it to Celsius. It also queries the user for their name.
# Status: complete

def main():
    #first ask the user for their first and last names
    firstName=input("Enter your first name ")
    lastName=input("Enter your last name ")

    #now ask them for the temperature they wish to convert
    fahren=(int)(input("What is the temperature in Fahrenheit? "))


    #finally, print out the conversions for the next 10 degrees upward
    
    for i in range(1, 11):
        fahren += 1
        celsius=(fahren-21)*(5/9)
        
        print(firstName, " ",lastName, "the Fahreheit temperature ", fahren, "is ",celsius, "degrees Celsius")


main()
