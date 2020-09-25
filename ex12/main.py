# -*- coding: utf-8 -*-
import math


# function that returns the set X
import sys


def getX():
    # init set X
    X = {'a', 'b', 'c', 'd'}

    return X


# function that returns the set Y
def getY():
    # init set Y
    Y = {'s', 'b', 'd'}

    return Y


# function that returns the display of the X and Y sets
def setsInitial(a, b):
    try:
        # set X
        X = a
        # set Y
        Y = b
        listX = []
        listY = []

        # init of the table containing the display of the X and Y sets
        res = []
        # init list from set X
        for i in X:
            listX.append(i)

        # init list from set Y
        for i in Y:
            listY.append(i)

        # sort the list
        listX = sorted(listX)

        # enriched the table res
        res.append("X : {'" + str(listX[0]) + "','" + str(listX[1]) + "', '" + str(listX[2]) + "', '" + str(listX[3]) + "'}")
        res.append("Y : {'" + str(listY[0]) + "','" + str(listY[1]) + "', '" + str(listY[2]) + "'}")

        # returns a string containing the display of the sets
        return res

    except Exception:
        raise Exception


# function which returns the display of the belonging operation
# between the 2 sets passed in parameter
def appartenance(a, b):
    # the character whose existence must be validated as a set
    char = a
    # init of the table containing the display of this function
    res = []

    try:
        # checks the valour of the set
        if b == 'X':
            f = getX()
        elif b == 'Y':
            f = getY()
        else:
            raise ValueError
        # checks the character in the set
        expression = char in f

        # enriched the table res
        res.append(str(char) + " in " + str(b) + " : " + str(expression))

        # returns a string containing the display of the operation between the character and the set
        return res

    except ValueError:
        print("ERROR")


# function that returns the display of the operation
# between two sets. The type of the operation, and the two sets are passed in parameter
def operation(a, b, c):
    type_operation = c
    res = {}
    # Init the first set
    if a == 'X':
        ensemble1 = getX()
    elif a == 'Y':
        ensemble1 = getY()
    else:
        raise ValueError
    # Init the second set
    if b == 'X':
        ensemble2 = getX()
    elif b == 'Y':
        ensemble2 = getY()
    else:
        raise ValueError
    # Realize operation in function of its type
    if type_operation == '-':
        res = ensemble1 - ensemble2
    elif type_operation == 'union':
        res = ensemble1.union(ensemble2)
    elif type_operation == 'inter':
        res = ensemble1.intersection(ensemble2)

    list_res = []
    for i in res:
        list_res.append(i)
    tailleRes = len(res)

    # Display of the operation
    msg = str(a) + " " + str(type_operation) + " " + str(b) + " : {"
    i = 0
    while i < tailleRes:
        msg = msg + "'" + str(list_res[i]) + "'"
        if i < (tailleRes - 1):
            msg = msg + ", "
        i = i + 1
    msg += "}"

    # returns a string containing the display of the operation
    return msg


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
            tab = setsInitial(getX(), getY())
            print(tab[0])
            print(tab[1])
            print(appartenance('c', 'X')[0])
            print(appartenance('a', 'Y')[0])
            print(operation('X', 'Y', '-'))
            print(operation('Y', 'X', '-'))
            print(operation('X', 'Y', 'union'))
            print(operation('X', 'Y', 'inter'))

        except Exception:
            print("ERROR")
        # close file
        file.close()
