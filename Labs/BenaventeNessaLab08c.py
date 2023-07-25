# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: July 4, 2023
# Description: This is Lab 8 part c, doubling the values of a list
# Status: complete


def findDoubles(lst):
    # Double the values of the list
    doubled_list = [num * 2 for num in lst]
    
    # Return the doubled list
    return doubled_list


def main():
    # Ask the user for 5 numbers and store them in a list
    numbers = []
    for i in range(5):
        number = int(input("Enter a number: "))
        numbers.append(number)
    
    # Call the findDoubles function to double the values of the list
    doubled_numbers = findDoubles(numbers)
    
    # Print the result
    print("Doubled numbers:", doubled_numbers)


# Call the main function to run the program
main()
