# -*- coding: utf-8 -*-
import math
import sys


# define a class with the name "MaClasse")
class MaClasse:

    # attributes of its Class
    x = 23
    y = x + 5

    # procedure that displays the values of y and z
    def affiche(self):
        z = 42
        print("(" + str(self.y) + ", " + str(z) + ")")


# main function
if __name__ == '__main__':
    try:
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        try:
            # instantiation of an object of the MyClasse class
            objet = MaClasse()
            # invocation of the object's function 'affiche'
            objet.affiche()
        except Exception:
            print("ERROR")

        # close file
        file.close()
