__author__ = 'Ciaran'

# Write a program avgword.py that computes the average word length for all the
# words in a file. Do not worry about punctuation, and ask the user for the file name.

def genRandomWord(filename):
    listOFWords = []
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                listOFWords.append(word)

    return listOFWords

def calcAv(listOFWords):
    total = 0
    for x in listOFWords:
        total += len(x)
        # print(total)
    avg = total / (len(listOFWords))

    print("The average length for a word in this file is :", int(avg))

def main():

    filename = input("Please enter file name carefully (if file is in separate folder, enter file location): ")
    listOfWords = genRandomWord(filename)
    calcAv(listOfWords)

main()