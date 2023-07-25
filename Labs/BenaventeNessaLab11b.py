# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: July 18, 2023
# Description: This is Lab 11 part b
# Status: complete

import random

def main():
    print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
    input()
    flips = 0
    heads = 0

    while flips < 1000:
        if random.randint(0, 1) == 1:
            heads = heads + 1
        flips += 1
        print('Number of heads:', heads)

        if flips == 900:
            print('900 flips and there have been', heads, 'heads.')
        if flips == 100:
            print('At 100 tosses, heads has come up', heads, 'times so far.')
        if flips == 500:
            print('Half way done, and heads has come up', heads, 'times.')

    print()
    print('Out of 1000 coin tosses, heads came up', heads, 'times!')
    print('Were you close?')


