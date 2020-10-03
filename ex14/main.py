"""
..module:: ex14
    :synopsis:: Définir une classe MaClasse possédant les attributs suivants :
            – données : deux attributs de classes : x = 23 et y = x + 5.
            – méthode : une méthode affiche contenant un attribut d’instance z = 42 
                        et les affichages de y et de z.
            – Dans le programme principal, instanciez un objet de la classe MaClasse
                        et invoquez la méthode affiche.
"""
import math
import sys


def ex14(self):
    """
     ..function: Procedure that displays the values of y and z

     """
    x = 23
    y = x + 5
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
