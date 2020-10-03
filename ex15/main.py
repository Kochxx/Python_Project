"""
..module:: ex15
    :synopsis:: Définir une classe Vecteur2D avec un constructeur
            fournissant les coordonnées par défaut d’un vecteur du plan
            (par exemple : x = 0 et y = 0). Dans le programme principal,
            instanciez un Vecteur2D sans paramètre, un Vecteur2D
            avec ses deux paramètres, et affichez- les
"""

import sys


class Vecteur2D:
    """
    ..class:: Class with the name "Vecteur2D"

    """

    # init class
    def __init__(self, cX=0.0, cY=0.0):
        """
            ..function: Init class

            :param cX: x coordinate
            :param cY: y coordinate
        """
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
                    print("par défaut : (x=" + str('{:.8f}'.format(vecteur.x)) + ", y=" + str('{:.8f}'.format(vecteur.y)) + ")")
                    print("instance : (x=" + str('{:.8f}'.format(vecteur2.x)) + ", y=" + str('{:.8f}'.format(vecteur2.y)) + ")")

                except Exception:
                    print("ERROR")

                # close file
                file.close()
