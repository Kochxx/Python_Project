# -*- coding: utf-8 -*-
"""
..module:: ex01
    :synopsis:: A l’aide de la fonction input(),
     affectez les variables temps et distance
     par les valeurs saisies par l’utilisateur.
     Calculez et affichez la valeur de la vitesse.
     Améliorez l’affichage enimposant un chiffre après le point décimal.
"""

import sys


def speed(a, b):
    """
        ..function: Function that calculates the speed from the time and distance
        passed as a parameter

        :param a: time value
        :param b: distance value

        :return v: the speed calculated
    """
    time = a
    dist = b
    try:
        # calculation of speed
        v = dist/time
    except ZeroDivisionError:
        print("ERROR")
    else:
        return v


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
                # separates arguments from a line
                tab = lines.split(";")
                # checks the number of arguments
                if len(tab) != 2:
                    raise Exception
                # retrieves the time argument from the line
                temps = float(tab[0])
                # retrieves the distance argument from the line
                dist = float(tab[1])

            except Exception:
                print("ERROR")

            else:
                try:
                    # print the speed with 8 digits after the decimal point
                    print('{:.8f}'.format(speed(temps, dist)))
                except Exception:
                    print("ERROR")
        # closed file INPUT.txt
        file.close()