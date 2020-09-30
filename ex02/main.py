
"""
..module:: ex02 
    :synopsis:: Saisissez un flottant. S’il est positif ou nul,
     affichez sa racine, sinon affichez un message d’erreur: 
     https://docs.python.org/3/library/math.html
"""

import math
import sys


class ex02:
    """
    ..class:: Class contains the function for the exercise 2

    """
    def squareRoot(self, a):
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
        ex2 = ex02()
        # reading the file
        for lines in file.readlines():
            try:
                # recovers the number of the line in the form of a float
                number = float(lines)
                # print the square root with 2 digits after the decimal point
                print('{:.2f}'.format(ex2.squareRoot(number)))
            except ValueError:
                print("ERROR")
        # close file INPUT.txt
        file.close()
