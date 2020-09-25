# -*- coding: utf-8 -*-
import math
import sys


# function that verifies the pressure and volume passed
# in parameter according to defined thresholds and returns the instructions
def secure(a, b):
    # pressure threshold
    pSeuil = 2.3
    # volume threshold
    vSeuil = 7.41
    pression = a
    volume = b
    try:
        # checks the pressure and the volume in relation to their threshold
        if (pression > pSeuil) & (volume > vSeuil):
            res = "KO"
        else:
            if pression > pSeuil:
                res = "Augmenter"
            else:
                if volume > vSeuil:
                    res = "Diminuer"
                else:
                    res = "OK"
        return res
    except Exception :
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
        # reading file
        for lines in file.readlines():
            try:
                # separates arguments from a line
                tab = lines.split(";")
                # checks the number of arguments
                if len(tab) != 2:
                    raise Exception
                # retrieves the pressure argument from the line
                a = float(tab[0])
                # retrieves the volume argument from the line
                b = float(tab[1])
            except ValueError:
                print("ERROR")
            else:
                try:
                    # print the instruction for the given volume and pressure
                    print(secure(a, b))
                except Exception:
                    print("ERROR")
        # close file
        file.close()
