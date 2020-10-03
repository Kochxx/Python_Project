"""
..module:: ex13
    :synopsis:: Écrire une fonction compterMots ayant un argument
        (une chaîne de caractères) et qui renvoie un dictionnaire 
        qui contient la fréquence de tous les mots de la chaîne entrée
"""
import sys


def compterMots(stringParam):
    """
    ..function: function taking a string, conting every occurence 
                of the words inside of it and returning said count
                in the form of a dictionary

    :param stringParam: string to be evaluated

    :return result, thedictionary with the count of all occurences
    """
    dictionary = {
    }
    # retrieves the words on the line currently read
    words = stringParam.split(" ")
    # checks the number of arguments
    if len(words) == 0:
        print("ERROR")
        raise Exception
    #used to remove the trailing \n at the end of the last word
    words[len(words) - 1 ] = words[len(words) - 1].rstrip()
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    result = {
    }
    dictionnary_keys = sorted(list(dictionary.keys()))

    for key in dictionnary_keys:
        result[key] = dictionary[key]
        
    return result

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
                # rstrip() is used to strip trailing EOL
                print(lines)
                # count the words in the string
                print(compterMots(lines))
            except ValueError:
                print("ERROR")
            except Exception:
                print("ERROR")
        # close file INPUT.txt
        file.close()
