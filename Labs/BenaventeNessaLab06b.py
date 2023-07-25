# Name: Nessa Benavente
# Class: CSCI 1411-001
# Due Date: June 27, 2023
# Description: This is Lab 6 part b, finding the Caesar cipher
# Status: complete


# The following functions will be for encoding and decoding messages, while preserving spaces

def encode(message, key):
    encoded_message = ""
    for ch in message:
        if ch == " ":
            encoded_ch = " "
        else:
            encoded_ch = chr(ord(ch) + key)
        encoded_message += encoded_ch
    return encoded_message


def decode(encoded_message, key):
    decoded_message = ""
    for ch in encoded_message:
        if ch == " ":
            decoded_ch = " "
        else:
            decoded_ch = chr(ord(ch) - key)
        decoded_message += decoded_ch
    return decoded_message


# The following code is the main code in which the user input will call the two functions above to meet the objectives of the lab

def main():
    # Ask for user input
    plaintext = input("Enter a string: ")
    key = int(input("Enter the key (integer): "))

    # Encode the message
    encoded_message = encode(plaintext, key)
    print("Encoded message:", encoded_message)

    # Decode the encoded message
    decoded_message = decode(encoded_message, key)
    print("Decoded message:", decoded_message)
