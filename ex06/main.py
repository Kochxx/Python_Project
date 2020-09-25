# -*- coding: utf-8 -*-
import math
import sys


# function which returns the cube of a number passed in parameter
def cube(a):
    num = a
    try:
        # calculate the cube of the number
        res = math.pow(num, 3)
        return res
    except Exception:
        raise Exception


# calculates the volume of a sphere of radius passed in parameter
def vSphere(a):
    r = a
    try:
        # volume sphere calculation
        res = 4 * math.pi * cube(r)
        return res
    except Exception:
        print("ERROR")


# main function
if __name__ == '__main__':
    try:
        # open file TEST.py
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        # reading the file
        for lines in file.readlines():
            try:
                # recovers the argument in the form of a float
                number = float(lines)
            except ValueError:
                print("ERROR")
            else:
                try:
                    # print the volume of the sphere
                    print(vSphere(number))
                except Exception:
                    print("ERROR")

        # close file TEST.py
        file.close()
