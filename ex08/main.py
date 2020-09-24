# -*- coding: utf-8 -*-
import math

# procedure that displays the time of arrival of the train according to its speed
def tchacatchac(a):
    v = a
    dist = 170
    hdepart = 9
    try:
        temps = float(dist)/float(v)
        h = int(temps)
        min = int(math.floor((temps-h)*60))
        h = h + hdepart
        print(str(v)+"km/h -> "+str(h)+":"+str(min))
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
