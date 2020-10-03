
"""
..module:: ex06
    :synopsis:: Écrire une fonction cube qui retourne le cube
     de son argument. Écrire une fonc tion volumeSphere
     qui calcule le volume d’une sphère de rayon r fourni
     en argument et qui utilise la fonction cube.
     Tester la fonction volumeSphere par un appel
     dans le programme principal décimal.
"""

import math
import sys


def cube(self, a):
    """
    ..function: Function that returns the cube of a number passed in parameter

    :param a: number to be cubed

    :return res: return a per cube
    """
    num = a
    try:
        # calculate the cube of the number
        res = math.pow(num, 3)
        return res
    except Exception:
        raise Exception

def ex06(self, a):
    """
    ..function: Function calculates the volume of a sphere of radius passed in parameter

    :param a: radius of the sphere
    
    :return res: return the volume of the sphere
    """
    r = a
    try:
        # volume sphere calculation
        res = 4 * math.pi * self.cube(r)
        return res
    except Exception:
        print("ERROR")


# main function
if __name__ == '__main__':
    try:
        # open file TEST.py
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        ex6 = ex06()
        # reading the file
        for lines in file.readlines():
            try:
                # recovers the argument in the form of a float
                number = float(lines)
            except ValueError:
                print("ERROR")
            else:
                try:
                    # print the volume of the sphere
                    print(ex6.vSphere(number))
                except Exception:
                    print("ERROR")

        # close file TEST.py
        file.close()
