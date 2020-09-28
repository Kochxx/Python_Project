"""
..module:: ex12
    :synopsis:: A l’aide de la fonction input(),
     affectez les variables temps et distance
     par les valeurs saisies par l’utilisateur.
     Calculez et affichez la valeur de la vitesse.
     Améliorez l’affichage enimposant un chiffre après le point décimal.
"""

import math


# function that returns the set X
import sys


class ex12:
    """
    ..class:: Class contains the functions for the exercise 12

    """
    def getX(self):
        """
        ..function: Function that returns the set X

        :return X: the set X
        """
        # init set X
        X = {'a', 'b', 'c', 'd'}

        return X

    def getY(self):
        """
        ..function: Function that returns the set Y

        :return Y: the set Y
        """
        # init set Y
        Y = {'s', 'b', 'd'}

        return Y

    def setsInitial(self, a, b):
        """
        ..function: Function that returns the display of the X and Y sets
        :param a: the set X
        :param b: the set Y
        :return res: a string containing the display of the sets
        """
        try:
            # set X
            X = a
            # set Y
            Y = b
            listX = []
            listY = []

            # init of the table containing the display of the X and Y sets
            res = []
            # init list from set X
            for i in X:
                listX.append(i)

            # init list from set Y
            for i in Y:
                listY.append(i)

            # sort the list
            listX = sorted(listX)

            # enriched the table res
            res.append("X : {'" + str(listX[0]) + "','" + str(listX[1]) + "', '" + str(listX[2]) + "', '" + str(listX[3]) + "'}")
            res.append("Y : {'" + str(listY[0]) + "','" + str(listY[1]) + "', '" + str(listY[2]) + "'}")

            # returns a string containing the display of the sets
            return res

        except Exception:
            raise Exception

    def appartenance(self, a, b):
        """
        ..function: Function which returns the display of the belonging operation
                    between the 2 sets passed in parameter
        :param a: character whose existence must be validated as a set
        :param b: the name of the set
        :return res: a string containing the display of the function
        """
        # the character whose existence must be validated as a set
        char = a
        # init of the table containing the display of this function
        res = []

        try:
            # checks the valour of the set
            if b == 'X':
                f = self.getX()
            elif b == 'Y':
                f = self.getY()
            else:
                raise ValueError
            # checks the character in the set
            expression = char in f

            # enriched the table res
            res.append(str(char) + " in " + str(b) + " : " + str(expression))

            # returns a string containing the display of the operation between the character and the set
            return res

        except ValueError:
            print("ERROR")

    def operation(self, a, b, c):
        """
        ..function: Function that returns the display of the operation
                    between two sets. The type of the operation,
                    and the two sets are passed in parameter
        :param a: the name of the set 1
        :param b: the name of the set 2
        :param c: character to define the type of operation
        :return res: a string containing the display of the operation
        """
        type_operation = c
        res = {}
        # Init the first set
        if a == 'X':
            ensemble1 = self.getX()
        elif a == 'Y':
            ensemble1 = self.getY()
        else:
            raise ValueError
        # Init the second set
        if b == 'X':
            ensemble2 = self.getX()
        elif b == 'Y':
            ensemble2 = self.getY()
        else:
            raise ValueError
        # Realize operation in function of its type
        if type_operation == '-':
            res = ensemble1 - ensemble2
        elif type_operation == 'union':
            res = ensemble1.union(ensemble2)
        elif type_operation == 'inter':
            res = ensemble1.intersection(ensemble2)

        list_res = []
        for i in res:
            list_res.append(i)
        tailleRes = len(res)

        # Display of the operation
        msg = str(a) + " " + str(type_operation) + " " + str(b) + " : {"
        i = 0
        while i < tailleRes:
            msg = msg + "'" + str(list_res[i]) + "'"
            if i < (tailleRes - 1):
                msg = msg + ", "
            i = i + 1
        msg += "}"

        # returns a string containing the display of the operation
        return msg


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
            ex_12 = ex12()
            tab = ex_12.setsInitial(ex_12.getX(), ex_12.getY())
            print(tab[0])
            print(tab[1])
            print(ex_12.appartenance('c', 'X')[0])
            print(ex_12.appartenance('a', 'Y')[0])
            print(ex_12.operation('X', 'Y', '-'))
            print(ex_12.operation('Y', 'X', '-'))
            print(ex_12.operation('X', 'Y', 'union'))
            print(ex_12.operation('X', 'Y', 'inter'))

        except Exception:
            print("ERROR")
        # close file
        file.close()
