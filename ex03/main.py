"""
..module:: ex03
    :synopsis:: Saisir deux mots, comparez-les pour trouver 
        le « plus petit » et affichez le résultat.
        L’ordre lexicographique est celui du dictionnaire
"""
import sys


# function that returns the smallest out of two words
def smallest(a, b):
    """
    ..function: function that returns the smallest out of two words

    :param a: first word
    :param b: second word

    :return the smallest word
    """
    firstStr = a.lower()
    secondStr = b.lower()
    if firstStr == secondStr:
        return firstStr
    elif firstStr < secondStr:
        return firstStr
    else:
        return secondStr


# main function
if __name__ == '__main__':
    # open file TEST.py
    try:
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        # reading the file
        for lines in file.readlines():
            try:
                # retrieves the pair of words on the line currently read
                tab = lines.split(";")
                # checks the number of arguments and them being empty or not
                if len(tab) != 2 or tab[0] == "" or tab[1] == "":
                    print("ERROR")
                    continue

                # stores both words in temporary variables for clarity
                # rstrip() is used to strip trailing EOL messing with equality
                firstWord = tab[0].rstrip()
                secondWord = tab[1].rstrip()
                # print the smallest word out of the two
                print(smallest(firstWord, secondWord))
            except ValueError:
                print("ERROR")
            except Exception:
                print("ERROR")
        # close file INPUT.txt
        file.close()
