# -*- coding: utf-8 -*-
import math

<<<<<<< HEAD

def comprehensionList():
    liste = []
    try:
        for i in range(0, 6):
            if i >= 2:
                liste.append(i+3)

        return liste
=======
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
>>>>>>> main
    except Exception:
        raise Exception


<<<<<<< HEAD
if __name__ == '__main__':
    try:
        print(comprehensionList())
=======
def vitesse():
    i = 100
    while i <= 300:
        tchacatchac(i)
        i = i+10


if __name__ == '__main__':
    try:
        vitesse()
>>>>>>> main
    except Exception:
        print("ERROR")
