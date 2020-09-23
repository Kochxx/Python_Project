# -*- coding: utf-8 -*-
import math


def secure(a, b):
    pSeuil = 2.3
    vSeuil = 7.41
    pression = a
    volume = b
    try:
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


if __name__ == '__main__':
    try:
        file = open("INPUT.TXT", "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        for lines in file.readlines():
            try:
                tab = lines.split(";")
                if len(tab) != 2:
                    raise Exception
                a = float(tab[0])
                b = float(tab[1])
            except ValueError:
                print("ERROR")
            else:
                try:
                    print(secure(a, b))
                except Exception:
                    print("ERROR")


        file.close()
