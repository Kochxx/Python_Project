# -*- coding: utf-8 -*-
import math


def comprehensionList():
    liste = []
    try:
        for i in range(0, 6):
            if i >= 2:
                liste.append(i+3)

        return liste
    except Exception:
        raise Exception


if __name__ == '__main__':
    try:
        print(comprehensionList())
    except Exception:
        print("ERROR")
