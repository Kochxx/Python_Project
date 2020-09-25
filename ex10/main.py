# -*- coding: utf-8 -*-
import math
import sys
from typing import List


# function that returns a comprehension list that adds 3
# to each item in a list from 0 to 5
# if the item is greater than or equal to 2
def comprehensionList():
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
            # displays the comprehension list
            print(comprehensionList())
        except Exception:
            print("ERROR")
