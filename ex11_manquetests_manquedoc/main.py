# -*- coding: utf-8 -*-
import sys


# function that returns the smallest out of two words
def sortList(firstString, secondString):
    result = []

    result = [firstElement + secondElement for firstElement in firstString for secondElement in secondString]

    return result
    


# main function
if __name__ == '__main__':
    print(sortList("abc","de"))