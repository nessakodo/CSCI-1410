###########################################################################
# Name: Vanessa Benavente
# Date: July 24, 2023
# Description: This program asks the user for the name of a file and a word.
#              It then reads the file and counts the number of times the
#              given word appears in the file. The program uses nested loops
#              to accomplish this task. The outer loop reads one line at a
#              time from the file, and the inner loop counts the occurrences
#              of the word in each line. The total count of occurrences is
#              then displayed at the end.
#
# Functions:
#   1) count_word_in_file(filename, word):
#      - Input: filename (str) - The name of the file to be read.
#               word (str) - The word to be counted in the file.
#      - Output: int - The total number of times the word appears in the file.
#      - Description: This function takes the filename and word as input
#                     parameters. It opens the file and reads its content
#                     line by line. For each line, it splits the line into
#                     words and counts the occurrences of the given word in
#                     the line. The function then returns the total count of
#                     occurrences of the word in the entire file.
#
# Usage: The user runs the program and is prompted to enter the name of the
#        file and the word to be counted. The program then displays the total
#        count of occurrences of the word in the file.
###########################################################################

def count_word_in_file(filename, word):
    try:
        with open(filename, 'r') as file:
            total_count = 0
            for line in file:
                count_in_line = 0
                words = line.split()
                for w in words:
                    if w == word:
                        count_in_line += 1
                total_count += count_in_line

        return total_count
    except FileNotFoundError:
        print("Error: File not found.")
        return 0

if __name__ == "__main__":
    filename = input("Enter the name of the file: ")
    word = input("Enter the word to count: ")

    count = count_word_in_file(filename, word)
    print(f"The word '{word}' appears {count} time(s) in the file '{filename}'.")
