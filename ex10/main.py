"""
..module:: ex10
    :synopsis:: Utilisez une liste en compréhension
     pour ajouter 3 à chaque élément d’une liste d’entiers de 0 à 5,
     mais seulement si l’élément est supérieur ou égal à 2
"""

import math
import sys
from typing import List


def ex10(self):
    """
    ..function: Function that returns a comprehension list that adds 3
                to each item in a list from 0 to 5
                if the item is greater than or equal to 2

    :return listC: the modified comprehension list
    """
    # initialisation of the comprehension list
    listC = []
    try:
        # creation of the comprehension list
        for i in range(0, 6):
            if i >= 2:
                listC.append(i+3)
        return listC
    except:
        print("ERROR")


# main function
if __name__ == '__main__':
    try:
        # open file
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        try:
            exo10 = ex10()
            # displays the comprehension list
            print(exo10.comprehensionList())
        except Exception:
            print("ERROR")
