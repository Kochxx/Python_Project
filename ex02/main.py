# -*- coding: utf-8 -*-
import math


def handling(a):
    num = a
    if num < 0:
        raise ValueError
    else:
        res = math.sqrt(num)
        return res


if __name__ == '__main__':
    try:
        file = open("INPUT.TXT", "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        for lines in file.readlines():
            try:
                number = float(lines)
                print('{:.2f}'.format(handling(number)))
            except ValueError:
                print("ERROR")

        file.close()
