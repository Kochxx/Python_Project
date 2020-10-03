
"""
..module:: ex02 
    :synopsis:: Saisissez un flottant. S’il est positif ou nul,
     affichez sa racine, sinon affichez un message d’erreur: 
     https://docs.python.org/3/library/math.html
"""

import math
import sys


def squareRoot(a):
    """
    ..function:: Function that returns the square root of a float 'a' passed as parameter

    :param a: number whose square root must be calculated
    
    :return res: return the square root of a if a>=0
    """

    num = a
    # checks if the number is not negative
    if num < 0:
        raise ValueError
    else:
        # calculate the square root
        res = math.sqrt(num)
        return res


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
                # recovers the number of the line in the form of a float
                number = float(lines)
                # print the square root with 8 digits after the decimal point
                print('{:.8f}'.format(squareRoot(number)))
            except ValueError:
                print("ERROR")
        # close file INPUT.txt
        file.close()
