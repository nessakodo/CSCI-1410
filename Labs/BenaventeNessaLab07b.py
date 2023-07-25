# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: July 4, 2023
# Description: This is Lab 7 part b, finding the average score
# Status: complete

import os
os.chdir("/Users/nessakodo/Documents/CSCI")


def main():
    print("This program creates an average for each student's quiz scores")

    scores = input("Please enter the name of the input file: ")
    
    # open the input file
    infile = open(scores, "r")

    # get the file names of output file
    outfileName = input("What file should the usernames go in? ")
    
    # open the output file
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        # get the data for each student
        data = line.split()
        name = data[0]
        scores = [int(score) for score in data[1:]]  # Convert scores to integers

        # calculate the average score
        average = sum(scores) / len(scores)
        
        # write it to the output file
        outfile.write(f"{name} {average}\n")
        print(f"{name} {average}\n")

    # close both files 
    infile.close() 
    outfile.close()
    print("Student score averages have been written to", outfileName)

main()

