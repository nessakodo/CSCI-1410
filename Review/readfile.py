def main():
    print ('Read one line at a time using loop')
    infile = open ('names.txt', 'r')
    for line in infile:
        print(line, end='')
    infile.close()
    print()
    
main()