# -*- coding: utf-8 -*-
import math


def tchacatchac(a):
    v = a
    heureD = 9
    Dist = 170
    try:
        temps = (Dist/v)
        print(v)
        print(Dist)
        print('{:f}'.format(temps))
    except Exception:
        raise Exception


def vitesse():
    i = 100
    while i <= 300:
        tchacatchac(i)
        i = i+10


if __name__ == '__main__':
    try:
        vitesse()
    except Exception:
        print("ERROR")
