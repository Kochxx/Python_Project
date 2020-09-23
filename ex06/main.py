# -*- coding: utf-8 -*-
import math


def cube(a):
    num = a
    try:
        res = math.pow(num,3)
        return res
    except Exception:
        raise Exception


def vSphere(a):
    r = a
    try:
        res = 4 * math.pi * cube(r)
        return res
    except Exception:
        print("ERROR")


if __name__ == '__main__':
    try:
        file = open("INPUT.TXT", "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        for lines in file.readlines():
            try:
                number = float(lines)
            except ValueError:
                print("ERROR")
            else:
                try:
                    print(vSphere(number))
                except Exception:
                    print("ERROR")

        file.close()
