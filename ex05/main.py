"""
..module:: ex05
    :synopsis:: Affichez les entiers de 0 à 15 non compris,
        de trois en trois, en utilisant une boucle for et
        l’instruction range().
"""

import sys


def printRange(start, end, a):
    """
    ..function:: function that prints integer in [start;end[ with a step of a

    :param start: starting integer
    :param end: end integer
    :param a: step
    
    :return res: list of integer matching condition
    """
    x = range(start, end, a)
    res = []
    for n in x:
        res.append(n)
    return res


# main function
if __name__ == '__main__':
    try:
        print(printRange(0, 15, 3))
    except:
        print("ERROR")
