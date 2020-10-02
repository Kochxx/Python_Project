"""
..module:: ex16
    :synopsis:: Enrichissez la classe Vecteur2D précédente en lui ajoutant
     une méthode d’affichage etune méthode de surcharge d’addition
     de deux vecteurs du plan. Dans le programme principal,
     instanciez deux Vecteur2D, affichez-les et affichez leur somm
"""
import sys


# define a class with the name "Vecteur2D")
class Vecteur2D:
    """
    ..class:: Class contains the function for the exercise 16

    """
def __init__(self, cX=0.0, cY=0.0, n=0):
    """
    ..function: init class

    :param cX: x coordinate
    :param cY: y coordinate
    :param n: number to define the type of vector ( the vector 1, 2 or the somme of the add function)
    """
    # x coordinate
    self.x = cX
    # y coordinate
    self.y = cY
    # number to define the type of vector ( the vector 1, 2 or the somme of the add function)
    self.num = n

def ex16(self):
    """
    ..function: displays vector
    """
    # print the vector like vector 1
    if self.num == 0:
        print("v1 : (x=" + str(self.x) + ", y=" + str(self.y) + ")")
    # print the vector like vector 'somme'
    elif self.num == -1:
        print("somme : (x=" + str(self.x) + ", y=" + str(self.y) + ")")
    else:
        # print the vector like other vector
        print("v" + str(self.num) + " : (x=" + str(self.x) + ", y=" + str(self.y) + ")")

def __add__(self, v2):
    """
    ..function: Function that adds two vectors
    :param v2: vector 2 to add

    """
    self.x = self.x + v2.x
    self.y = self.y + v2.y
    self.num = -1


# main function
if __name__ == '__main__':
    try:
        # open file
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR1")
    else:
        # reading the file
        for lines in file.readlines():
            try:
                # cuts the line in half starting from the symbol ','
                tab = lines.split(",")
                if len(tab) != 2:
                    raise Exception
                # cuts the line in half starting from the symbol ';'
                tab1 = tab[0].split(";")
                if len(tab1) != 2:
                    raise Exception
                # cuts the line in half starting from the symbol ';'
                tab2 = tab[1].split(";")
                if len(tab2) != 2:
                    raise Exception
                # defines the x coordinate of vector 1
                x1 = float(tab1[0])
                # defines the y coordinate of vector 1
                y1 = float(tab1[1])
                # defines the x coordinate of vector 2
                x2 = float(tab2[0])
                # defines the y coordinate of vector 2
                y2 = float(tab2[1])

                # instantiation vector 1
                vecteur1 = Vecteur2D(x1, y1)
                # instantiation vector 1
                vecteur2 = Vecteur2D(x2, y2, 2)
                # display vector 1
                vecteur1.affichage()
                # display vector 2
                vecteur2.affichage()
                # calculate add
                vecteur1.__add__(vecteur2)
                # display vector somme
                vecteur1.affichage()

            except Exception:
                print("ERROR")

            # close file
            file.close()
#
