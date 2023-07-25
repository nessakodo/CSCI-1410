# Vanessa
# Benavente
# June 27, 2023
# Lab 5. This lab shows various operations of String datatype

def main():
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")

    # You can calculate the size/length of the string using len() function

    length = len(firstName)
    print("length of the first name is:", length)

    length_2 = len(lastName)
    print("length of your last name is:",length_2)

    # "+" operator is used to concatenate 2 strings

    fullName = firstName + " " + lastName
    print("Your full name is ", fullName)

    # "*" operator is used as a repetition operator to make multiple copies of a string

    n = int(input("Enter a number: "))
    print("Repeating your name",n, "times")
    print((firstName+" ")*n)

   # You can iterate through the characters using for loop
    

    print("Printing the full name using for loop")
    for ch in fullName:
        print(ch, end = "")

    
     # A string is a sequence of character. Each individual character can be accessed by using index. In Python index starts from 0.
     # Here is an example how we can run a loop to access all characters from a string.
    

    print("\nPrinting the full name using indexing")
    for i in range(len(fullName)):
        print(fullName[i], end = "")

    
    # Python also allows indexing from right end of a string using negative indexes.
    # Negative indexing starts from -1.
    # Here is an example how we can use negative indexing to access the characters in reverse order.
    

    print("\nPrinting the name in reverse order")
    for i in range(-1, -(len(fullName)+1), -1):
         print(fullName[i], end = "")

    
    # Slicing operator is used to access a contiguous sequence of characters or substring. The following is an example of generating username from using the first 3 characters of the last name combined with the first 3 characters of the first name.
    

    userName = lastName[0:3] + firstName[0:3]
    print("\nYour username is: ",userName)
