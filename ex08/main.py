# -*- coding: utf-8 -*-
import math
import sys


# procedure that return the time of arrival of the train
# according to its speed passed in parameter
def tchacatchac(a):
    # train speed
    v = a
    # distance to go
    dist = 170
    # train departure time 9h00
    hdepart = 9
    try:
        # calculation of train travel time based on speed and distance to be covered
        temps = float(dist)/float(v)
        # number of hours of travel time
        h = int(temps)
        # number of minutes of travel time
        min = int(math.floor((temps-h)*60))
        # Arrival time
        h = h + hdepart
        # stocks the speed of the train and the arrival time associated
        res = (str(v)+"km/h -> "+str(h)+":"+str(min))
        # return the time of train's arrival
        return res
    except Exception:
        raise Exception


# function that returns the speed of the train from 100km/h to 300km/h
# in 10km/h steps on a table
def vitesse():
    i = 100
    tab = []
    # use the tchacatchac() function by 10km/h steps
    while i <= 300:
        tab.append(tchacatchac(i))
        i = i+10
    return tab


# main function
if __name__ == '__main__':
    try:
        # open file
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        try:
            # generates the train's arrival board
            table = vitesse()
            # print the train's arrival board
            for i in table:
                print(i)
        except Exception:
            print("ERROR")
        # close file INPUT.txt
        file.close()
