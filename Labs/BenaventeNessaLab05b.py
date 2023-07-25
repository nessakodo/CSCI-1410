# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: June 27, 2023
# Description: This is Lab 5 part b, generating a username and email address
# Status: complete

def main():
    # asking input for first name
    firstName = input("Please enter your first name: ")
    # asking input for last name
    lastName = input("Please enter your last name: ")
    # definiting username according to lab instructions
    userName = lastName.lower() + firstName[0].lower()
    print("\nYour username is: ",userName)
    # defining email address according to lab instructions
    emailAddress = firstName.lower() + "." + lastName.lower() + "@ucdenver.edu"
    print("\nYour email address is: ",emailAddress)
    
main()
