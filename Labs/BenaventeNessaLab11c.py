# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: July 18, 2023
# Description: This is Lab 11 part c
# Status: complete

import os
os.chdir("/Users/nessakodo/Documents/CSCI")

def main():
    count = 0
    sum = 0

    try:
        infile = open('data2.txt', 'r')

        line = infile.readline()
        while line != "":
            my_list = line.split(',')
            for num in my_list:
                sum = sum + float(num)
                count = count + 1
            line = infile.readline()

        infile.close()

        average = sum / count

        print('Number of data:', count)
        print('Sum of numbers is:', sum)
        print('Average is: {0:.2f}'.format(average))

    except FileNotFoundError:
        print("Error: File 'data2.txt' not found.")
    except ValueError:
        print("Error: Invalid data in the file.")
