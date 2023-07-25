def main():
    print("Read one line at a time using a loop")
    infile = None  # Initialize the infile variable before the try block
    try:
        infile = open('farh.txt', 'r')  # Replace 'fahr.txt' with your desired filename

        for line in infile:
            user_input = input(f"Read this line: '{line.strip()}'? (y/n): ")
            if user_input.lower() != 'y':
                break

    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")
    finally:
        if infile is not None:
            infile.close()  # Ensure the file is closed only if it was opened successfully

    print("Loop terminated.")

main()
