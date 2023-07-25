# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: June 27, 2023
# Description: This is Lab 6 part a, demonstrating various functions of String datatype
# Status: complete

def main():

    # Python translates each character to a number. The ord() function in python accepts a single character string as an argument and returns the numeric code of it.

    ch = input("Please enter a single character: ")
    value = ord(ch)
    print("The numeric representation of", ch, "is", value)

    # The chr() function does the reverse, taking an integer number as an argument and returing the equivelant character

    print("The equivelant character of the number", value, "is", chr(value))

    # The following piece of code will take a string as an input and it will convert each of the characters as a sequence of numbers (separated by whitespace)

    txt = input("Please enter a text: ")
    for ch in txt:
        print(ord(ch), end=" ")

    # split function splits a string into a list of substrings based on a delimiter

    txt1 = input("\nPlease enter a string with space: ")
    listSubStrings = txt1.split(" ")
    print(listSubStrings)

    # join function joins the lsit of strings into one string using a delimiter

    newString = "-".join(listSubStrings)
    print(newString)
