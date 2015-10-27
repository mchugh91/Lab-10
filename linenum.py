__author__ = 'Ciaran'

# Write a program linenum.py that asks for the name of a file and then prints
# the contents of the file with line numbers along the left edge.

def numberLines(filename):
    with open(filename, "r") as f:
        for line, i in enumerate(f):
            print(line, i)


def main():

    filename = input("Please enter file name carefully (if file is in separate folder, enter file location): ")
    numberedLines = numberLines(filename)
    print(numberedLines)

main()