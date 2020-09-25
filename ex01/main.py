# -*- coding: utf-8 -*-
import sys


#function that calculates the speed from the time and distance passed as a parameter
def handling(a, b):
    time = a
    dist = b
    try:
        #division
        v = dist/time
    except ZeroDivisionError:
        print("ERROR")
    else:
        return v

#main function
if __name__ == '__main__':
    #open file TEST.py
    try:
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        #reading the file
        for lines in file.readlines():
            try:
                #separates arguments from a line
                tab = lines.split(";")
                #checks the number of arguments
                if len(tab) != 2:
                    raise Exception
                #retrieves the time argument from the line
                temps = float(tab[0])
                #retrieves the distance argument from the line
                dist = float(tab[1])

            except Exception:
                print("ERROR")

            else:
                try:
                    #print the speed separates arguments from a line
                    print('{:.1f}'.format(handling(temps, dist)))
                except Exception:
                    print("ERROR")
        #closed file INPUT.txt
        file.close()
