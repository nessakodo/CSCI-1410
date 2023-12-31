# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: June 27, 2023
# Description: This is Lab 7 part a, showing techniques of reading and writing text files
# Status: complete

import os
os.chdir("/Users/nessakodo/Documents/CSCI")


def main():
    print("This program creates a file of emails and usernames from a file of names")
    
    # open the input file
    infile = open("in.txt", "r")

    # get the file names of output file
    outfileName = input("What file should the usernames go in? ")
    
    # open the output file
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create the ucdenver email address
        email = (first + "." + last).lower() + "@ucdenver.edu" 
        uname = (last[:]+first[0]).lower()
        # write it to the output file
        print(email + " " + uname)
        print(email + " " + uname, file=outfile)
    # close both files 
    infile.close() 
    outfile.close()
    print("Emails and usernames have been written to", outfileName)




