# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: July 4, 2023
# Description: This is Lab 8 part b, using dateConvert to convert date formats
# Status: complete


def dateConvert(date):
    # Split the date into month, day, and year
    month, day, year = date.split('/')
    
    # Create a list of month names
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    # Convert the month from string to integer
    month = int(month)
    
    # Convert the day from string to integer
    day = int(day)
    
    # Create the converted date format
    converted_date = f"{month_names[month - 1]} {day}, {year}"
    
    # Return the converted date
    return converted_date


def main():
    # Ask the user for a date input
    date_input = input("Enter a date (mm/dd/yyyy): ")
    
    # Call the dateConvert function to convert the date format
    converted_date = dateConvert(date_input)
    
    # Print the converted date
    print("Converted date:", converted_date)


# Call the main function to run the program
main()
