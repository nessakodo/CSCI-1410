##############################################################
# Function Name: read_data
# Description: Reads a set of numbers from an input file.
# Parameter: file_name - name of the input file
# Returns list of numbers
##############################################################

import os
os.chdir("/Users/nessakodo/Documents/CSCI")

import math

def read_data(file_name):
    # Open the file for reading
    with open(file_name, 'r') as file:
        # Initialize an empty list
        list_of_numbers = []

        # Use a definite loop to read each line of the file
        for line in file:
            # Convert the line into an integer
            number = int(line.strip())
            
            # Add the integer to the list
            list_of_numbers.append(number)

    # Close the file
    file.close()

    # Return the list
    return list_of_numbers

# Ask the user to input the file name
file_name = input("Enter the name of the input file: ")

# Call the read_data function with the user-provided file name
result = read_data(file_name)
print(result)


##############################################################
# Function Name: compute_sum
# Description: Calculates the sum of numbers in a list.
# Parameter: numbers - list of integer numbers
# Returns: sum of the numbers in the list
##############################################################
def compute_sum(numbers):
    # Initialize sum to 0
    sum = 0

    # Use a definite loop to add the numbers in the given list
    for number in numbers:
        sum += number

    # Return the sum
    return sum



# Call the read_data function with the user-provided file name
numbers_list = read_data(file_name)

# Call the compute_sum function with the numbers list
sum_of_numbers = compute_sum(numbers_list)

# Print the sum
print("Sum of numbers:", sum_of_numbers)

##############################################################
# Function Name: compute_mean
# Description: Calculates the mean of numbers in a list.
# Parameter: numbers - list of integer numbers
# Returns: mean of the numbers in the list
##############################################################
def compute_mean(numbers):
    # Calculate the sum of numbers using compute_sum function
    sum_of_numbers = compute_sum(numbers)

    # Calculate the size of the list
    list_size = len(numbers)

    # Divide sum of the numbers by the size of the list to compute the mean
    mean = sum_of_numbers / list_size

    # Return the mean
    return mean


# Call the read_data function with the user-provided file name
numbers_list = read_data(file_name)

# Call the compute_mean function with the numbers list
mean_of_numbers = compute_mean(numbers_list)

# Print the mean
print("Mean of numbers:", mean_of_numbers)

##############################################################
# Function Name: compute_sd
# Description: Calculates the standard deviation of numbers in a list.
# Parameter: numbers - list of integer numbers
# Returns: standard deviation of the numbers in the list
##############################################################
def compute_sd(numbers):
    # Calculate the mean of numbers using compute_mean function
    mean = compute_mean(numbers)

    # Initialize sum to 0
    sum = 0

    # Use a definite loop to calculate the sum of squared deviations
    for num in numbers:
        # Calculate the deviation by subtracting the mean from the num
        deviation = num - mean

        # Calculate the square of the deviation
        deviation_squared = deviation ** 2

        # Add the square of the deviation to the sum
        sum += deviation_squared

    # Calculate the size of the list
    list_size = len(numbers)

    # Divide the sum by the size-1 to compute the result
    result = sum / (list_size - 1)

    # Take the square root of the result to compute the standard deviation
    standard_deviation = math.sqrt(result)

    # Return the standard deviation
    return standard_deviation


# Call the read_data function with the user-provided file name
numbers_list = read_data(file_name)

# Call the compute_mean function with the numbers list
mean_of_numbers = compute_mean(numbers_list)

# Call the compute_standard_deviation function with the numbers list
standard_deviation_of_numbers = compute_sd(numbers_list)

# Print the mean and standard deviation
print("Mean of numbers:", mean_of_numbers)
print("Standard deviation of numbers:", standard_deviation_of_numbers)



##############################################################
# Function Name: write_result
# Description: Writes the result (sum, mean, and standard deviation) into an output file.
# Parameter: file_name - name of the output file
#            sum_val - sum of the numbers
#            mean_val - mean of the numbers
#            std_dev_val - standard deviation of the numbers
# Returns: None
##############################################################
def write_result(file_name, sum_val, mean_val, std_dev_val):
    # Open the file for writing
    with open(file_name, 'w') as file:
        # Write the result with appropriate labels and formatting
        file.write(f"Sum is: {sum_val:.2f}\n")
        file.write(f"Mean is: {mean_val:.2f}\n")
        file.write(f"Standard Deviation is: {std_dev_val:.2f}")

    # Close the file
    file.close()

# Call the read_data function with the user-provided file name
numbers_list = read_data(file_name)

# Call the compute_mean function with the numbers list
mean_of_numbers = compute_mean(numbers_list)

# Call the compute_standard_deviation function with the numbers list
standard_deviation_of_numbers = compute_sd(numbers_list)

# Call the compute_sum function with the numbers list
sum_of_numbers = compute_sum(numbers_list)

# Ask the user to input the name of the output file
output_file_name = input("Enter the name of the output file: ")

# Call the write_result function with the result values
write_result(output_file_name, sum_of_numbers, mean_of_numbers, standard_deviation_of_numbers)

print("Result written to the output file.")
