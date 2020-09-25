# -*- coding: utf-8 -*-

import sys


# define a class with the name "Vecteur2D")
class Vecteur2D:

    # init class
    def __init__(self, cX = 0.0, cY = 0.0):
        self.x = cX
        self.y = cY


# main function
if __name__ == '__main__':
    try:
        # open file
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        # reading the file
        for lines in file.readlines():
            try:
                # separates arguments from a line
                tab = lines.split(";")
                # checks the number of arguments
                if len(tab) != 2:
                    raise Exception
                # retrieves the x argument from the line
                x = float(tab[0])
                # retrieves the y argument from the line
                y = float(tab[1])

            except Exception:
                print("ERROR")

            else:
                try:
                    # instantiation without paramaters
                    vecteur = Vecteur2D()
                    # instantiation with paramaters
                    vecteur2 = Vecteur2D(x, y)
                    print("par défaut : (x=" + str(vecteur.x) + ", y=" + str(vecteur.y) + ")")
                    print("instance : (x=" + str(vecteur2.x) + ", y=" + str(vecteur2.y) + ")")

                except Exception:
                    print("ERROR")

                # close file
                file.close()
