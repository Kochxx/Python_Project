# -*- coding: utf-8 -*-
import math


def getX():
    X = {'a', 'b', 'c', 'd'}
    return X


def getY():
    Y = {'s', 'b', 'd'}
    return Y


def setsfunction(a, b):
    try:
        X = a
        Y = b
        listX = []
        listY = []
        for i in X:
            listX.append(i)
        for i in Y:
            listY.append(i)
        listX = sorted(listX)
        print("X : {'" + str(listX[0]) + "','" + str(listX[1]) + "', '" + str(listX[2]) + "', '" + str(listX[3]) + "'}")
        print("Y : {'" + str(listY[0]) + "','" + str(listY[1]) + "', '" + str(listY[2]) + "'}")
    except Exception:
        raise Exception


def appartenance(a, b):
    char = a
    try:
        if b == 'X':
            f = getX()
        elif b == 'Y':
            f = getY()
        else:
            raise ValueError
        expression = char in f
        print(str(char) + " in " + str(b) + " : " + str(expression))
    except ValueError:
        print("ERROR")


def operation(a, b, c):
    type_operation = c
    res = {}
    #1er Ensemble
    if a == 'X':
       ensemble1 = getX()
    elif a == 'Y':
        ensemble1 = getY()
    else:
        raise ValueError
    #2eme Ensemble
    if b == 'X':
       ensemble2 = getX()
    elif b == 'Y':
        ensemble2 = getY()
    else:
        raise ValueError
    #Operation
    if type_operation == '-':
        res = ensemble1 - ensemble2
    elif type_operation == 'union':
        res = ensemble1.union(ensemble2)
    elif type_operation == 'inter':
        res = ensemble1.intersection(ensemble2)

    listRes = []
    for i in res:
        listRes.append(i)
    tailleRes = len(res)

    #Affichage
    msg = str(a) + " " + str(type_operation) + " " + str(b) + " : {"
    i = 0
    while i < tailleRes:
        msg = msg+"'" + str(listRes[i]) + "'"
        if i < (tailleRes - 1):
            msg = msg+", "
        i = i + 1
    msg += "}"
    print(msg)


if __name__ == '__main__':
    try:
        setsfunction(getX(), getY())
        appartenance('c', 'X')
        appartenance('a', 'Y')
        operation('X', 'Y', '-')
        operation('Y', 'X', '-')
        operation('X', 'Y', 'union')
        operation('X', 'Y', 'inter')
    except Exception:
        print("ERROR")
