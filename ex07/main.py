# -*- coding: utf-8 -*-
"""
..module:: ex07
    :synopsis:: Écrire une fonction maFonction
        qui retourne f (x)= 2x^3+ x -5.
        Écrire une procédure tabuler avec quatre paramètres :
        fonction, borneInf, borneSupet nbPas.
        Cette procédure affiche les valeurs de fonction,
        de borneInf à borneSup,tous les nbPas.
        Elle doit respecter borneInf <borneSup.
        Tester cette procédure par un appel
        dans le programme principal après avoir saisi les deux bornes
        et le nombre de pas
"""

import sys
import math

def maFonction(self, x):
    """
    ..function: Function that returns the value of x after the treatment

    :param x: value x in int

    :return res: the value in int
    """
    res = 2 * math.pow(x, 3) + x - 5
    return int(res)

def ex07(self, fonction, borneInf, borneSup, nbPas):
    """
    ..function: Function that returns the value of the function
                between the terminals per steps

    :param borneInf: value of the minimal terminal, in int
    :param borneSup: value of the maximal terminal, in int
    :param nbPas: value of the number per step
    
    :return res: return the value of the function
                between the terminals per steps
    """
    bI = int(borneInf)
    bS = int(borneSup)
    nb = int(nbPas)
    res = []
    if nbPas == 0:
        raise ValueError
    elif bI < bS:
        for x in range(bI, bS, nb):
            mafonction = "self."+fonction + "(" + str(x) + ")"
            res.append(eval(mafonction))
    else:
        raise ValueError
    return res

# main function
if __name__ == '__main__':
    # open file INPUT.txt
    try:
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR 1")
    else:
        # reading the file
        for lines in file.readlines():
            try:
                tab = lines.split(";")
                # checks the number of arguments and them being empty or not
                if len(tab) != 4 or tab[0] == "" or tab[1] == "" or tab[2] == "" or tab[3] == "":
                    raise ValueError
                else:
                    f = tab[0]
                    borneInf = tab[1]
                    borneSup = tab[2]
                    nbPas = tab[3]
                    print(ex07(f, borneInf, borneSup, nbPas))
            except ValueError:
                print("ERROR 2")
            except Exception:
                print("ERROR 3")
        # close file INPUT.txt
        file.close()
