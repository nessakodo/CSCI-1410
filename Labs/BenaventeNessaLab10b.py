##############################################################
# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: July 18, 2023
# Description: This is lab 10 part b, calculcating the final price in relation to quantity.
##############################################################



##############################################################
# Function Name: discount_percentage
# Description: Calculate the discount percentage based on the quantity of packages purchased.
#              The discount percentage is determined as follows:
#              - 40% for quantities greater than or equal to 100
#              - 30% for quantities greater than or equal to 50
#              - 20% for quantities greater than or equal to 20
#              - 10% for quantities greater than or equal to 10
#              - 0% for all other quantities
# Parameter: quantity - Number of packages purchased
# Returns: Discount percentage as an integer value
##############################################################

def discount_percentage(quantity):
    if quantity >= 100:
        return 50
    elif quantity >= 50:
        return 40
    elif quantity >= 20:
        return 30
    elif quantity >= 10:
        return 20
    else:
        return 0

def main():
    try:
        quantity = int(input("Enter the number of packages purchased: "))

        if quantity < 0:
            print("Error: Quantity cannot be negative.")
        else:
            discount_percent = discount_percentage(quantity)
            amount = quantity * 99
            discount_amount = amount * discount_percent / 100
            total_amount = amount - discount_amount

            print("Discount Percentage:", discount_percent, "%")
            print("Discount Amount: ${0:.2f}".format(discount_amount))
            print("Total Amount: ${0:.2f}".format(total_amount))

    except ValueError:
        print("Error: Invalid input. Please enter a valid quantity.")

if __name__ == "__main__":
    main()
